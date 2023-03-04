from django.shortcuts import render
from .models import Account, UserType
from seeker.models import SeekerProfile
from recruiter.models import Company
from superuser.models import AdminProfile, CompanyCategory
from rest_framework import generics
from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .token import create_jwt_pair_tokens
from accounts.otp import send_otp, verify_otp
import datetime
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


    def post(self, request : Request):
        data = request.data
        print(data)

        serializer = self.serializer_class(data=data)

        user_type = request.data.get('user_type')
        email = request.data.get('email')


        if serializer.is_valid():
            serializer.save()

            print('serializer is valid')

            if user_type == 'JobSeeker':
                print('role is seeker')
                user = Account.objects.get(email = email)
                user_type = UserType.objects.get(user_type_name = 'JobSeeker')
                user.user_type = user_type
                user.save()
                print(user.user_type)
                SeekerProfile.objects.create(seeker = user)
                phone_number = data.get('phone_number')
                send_otp(phone_number)
                print('otp sent')

            elif user_type == 'Recruiter':
                print('role is recruiter')
                user = Account.objects.get(email = email)
                user_type = UserType.objects.get(user_type_name = 'Recruiter')
                user.user_type = user_type
                user.is_staff = True
                user.save()
                print(user.first_name)

                company_name = data.get('company_name')
                company_category = data.get('company_category')

                print(company_name, company_category)
         
                category = CompanyCategory.objects.get(category_name=company_category)
                company = Company.objects.create(recruiter=user,company_name = company_name, category = category)

                print('saved')

                # Generate employer id
                yr = int(datetime.date.today().strftime('%Y'))
                dt = int(datetime.date.today().strftime('%d'))
                mt = int(datetime.date.today().strftime('%m'))
                d = datetime.date(yr,mt,dt)
                current_date = d.strftime("%Y%m%d")
                employer_id = current_date + str(company.id)
                company.employer_id = employer_id
                company.save()



                phone_number = data.get('phone_number')
                send_otp(phone_number)
                print('otp send')



            else:
                print('neither seeker nor recruiter')
                user = Account.objects.get(email=email)
                AdminProfile.objects.create(admin=user)
            
            response = {
                'message' : 'User Created Successfully',
                'otp' : True
            }
            print('sneding response')
            return Response(data = response, status = status.HTTP_201_CREATED)

        else:
            print('serializer not valid')
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Verify_otpView(APIView):

    def post(self, request : Request):
        data = request.data
        check_otp = data.get('otp')
        print('verify otp')
        phone_number = data.get('mobile')
        print(phone_number, check_otp)
        print("here")
        check = verify_otp(phone_number, check_otp)
        # check = True

        if check:
            user = Account.objects.get(phone_number = phone_number)
            user.is_verified = True
            user.save()
            print("done")

            return Response(
                data= ({'Success' : 'User is verified', 'is_verified' : True}), status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"Failed" : "user is Not verified "}, status=status.HTTP_400_BAD_REQUEST
            )



class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)

        user = authenticate(request, email = email, password = password)

        print(user)

        if user is not None:
            if user.is_verified == True:
                print('authenicated')
                tokens = create_jwt_pair_tokens(user)
                profile = {}

                if user.user_type.user_type_name == 'JobSeeker':
                    profile = SeekerProfile.objects.get(seeker=user)
                elif user.user_type.user_type_name == 'Recruiter':
                    profile = Company.objects.get(recruiter=user)
                else:
                    if not AdminProfile.objects.filter(admin = user):
                        AdminProfile.objects.create(admin=user)
                    profile = AdminProfile.objects.get(admin = user)

                response = {
                    "message" : "Login Successful",
                    "token" : tokens,
                    "profile_id" : profile.id,
                    "is_login" : True,
                    "user" : {
                        "user_id" : user.id,
                        "email" : user.email,
                        "user_type" : user.user_type.user_type_name,
                        "profile_id" : profile.id
                    }
                }
                return Response(data=response, status=status.HTTP_200_OK)
            
            else:
                response = {
                    "message" : "user is not verified"
                }
                return Response(data=response, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        else:
            return Response(data={"message" : "Invalid email or password !"}, status=status.HTTP_400_BAD_REQUEST)




class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request:Response):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logged out successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class ForgotPasswordView(APIView):
    
    def post(self, request:Response):
        email = request.data['email']
        if Account.objects.filter(email=email).exists:
            user = Account.objects.get(email=email)
            password = request.data['password']
            user.set_password(password)
            user.save()

            return Response({"message": "Password resetted succesfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "User with this email does not exists!. Please Signup"}, status=status.HTTP_400_BAD_REQUEST)


