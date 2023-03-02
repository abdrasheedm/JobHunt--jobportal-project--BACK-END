from django.shortcuts import render
from .serializers import (CompanyCategorySerializer, CategoryDepartmentSerializer, AlluserViewSerializer, CategoryDepartmentPostSerializer, NotificationSerializer, PaymentDetailSerializer,
                          QualificationSerializer)
from rest_framework.viewsets import ModelViewSet
from .models import CompanyCategory, CompanyDepartment, PaymentDetails
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import Account
from recruiter.serilaizers import JobSerializerGet
from recruiter.models import Job, Qualification, Company
from seeker.models import SeekerProfile
from notifications.models import Notifications
from django.db.models import Sum


# Create your views here.

class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class SingleCategoryView(APIView):

    def get(self, request:Response):
        cat_id = request.query_params['cat_id']
        try:
            instance = CompanyCategory.objects.get(id=cat_id)
            serialzers = CompanyCategorySerializer(instance=instance, many=False)
            return Response(data=serialzers.data, status=status.HTTP_200_OK)
        
        except:
            return Response({"message" : "Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class CategoryAddView(APIView):
    # permission_classes = [IsAdminUser]

    def post(self, request:Response):
        serializer = CompanyCategorySerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Category added successfully"}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"message" : "Category creation failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class CategorUpdateView(APIView):
    # permission_classes = [IsAdminUser]

    def patch(self, request:Response):
        print(request)
        cat_id = request.query_params['cat_id']
        try:
            print(cat_id)
            instance = CompanyCategory.objects.get(id = cat_id)
            print(request.data, '--------')
            instance.category_name = request.data['category_name']
            instance.save()

            return Response({"message" : "Category Updated"}, status=status.HTTP_200_OK)

        except:
            return Response({"message" : "Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryRemoveView(APIView):
     # permission_classes = [IsAdminUser]

    def post(self, request:Response):
        cat_id = request.query_params['cat_id']
        try:
            instance = CompanyCategory.objects.get(id = cat_id)
            instance.delete()

            return Response({"message" : "Category Deleted"}, status=status.HTTP_200_OK)

        except:
            return Response({"message" : "Data not found"}, status=status.HTTP_400_BAD_REQUEST)




class AllDepartmentView(ModelViewSet):
    queryset = CompanyDepartment.objects.all()
    serializer_class = CategoryDepartmentSerializer



class CompanyDepartmentView(APIView):
    

    def get(self, request:Response):

        try:
            id = request.query_params['id']
            print(request.data)
            category = CompanyCategory.objects.get(id = id)
            departments = CompanyDepartment.objects.filter(category=category)

            serializer = CategoryDepartmentSerializer(departments, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except:
            departments = CompanyDepartment.objects.all()
            serializer = CategoryDepartmentSerializer(departments, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        

class AddDepartmentView(APIView):
    # permission_classes = [IsAdminUser]
    def post(self, request:Response):
        serializers = CategoryDepartmentPostSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"message" : "Department added succesfully"}, status=status.HTTP_200_OK)        
        else:
            print(serializers.errors)
            return Response({"message" : "Department creattion failed"}, status=status.HTTP_400_BAD_REQUEST)



class UpdateDepartmentView(APIView):
    # permission_classes = [IsAdminUser]        

    def patch(self, request:Response):
        dep_id = request.query_params['dep_id']
        try:
            instance = CompanyDepartment.objects.get(id=dep_id)
            serializers = CategoryDepartmentPostSerializer(instance=instance,data=request.data, partial =True)


            if serializers.is_valid():
                serializers.save()
                return Response({"message" : "Department updated succesfully"}, status=status.HTTP_200_OK)        
            else:
                print(serializers.errors)
                return Response({"message" : "Department updation failed"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"message": "data not found"}, status=status.HTTP_400_BAD_REQUEST)
        



class RemoveDepartmentView(APIView):
    # permission_classes = [IsAdminUser]        

    def get(self, request:Response):
        dep_id = request.query_params['dep_id']
        try:
            instance = CompanyDepartment.objects.get(id=dep_id)
            instance.delete()

            return Response({"message": "Department removed"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"message": "data not found"}, status=status.HTTP_400_BAD_REQUEST)
        

class SingleDepartmentView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request:Response):
        dep_id = request.query_params['dep_id']
        try:
            instance = CompanyDepartment.objects.get(id= dep_id)
            serializer = CategoryDepartmentSerializer(instance=instance, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response({"message" : "data not found"}, status=status.HTTP_400_BAD_REQUEST)

            



class AllUserGet(ModelViewSet):
    print(Response, '-----------------------------')
    permission_classes = [IsAdminUser]
    
    queryset = Account.objects.all()
    serializer_class = AlluserViewSerializer


class BlockUnBlockUserView(APIView):
    # permission_classes = [IsAdminUser]

    def post(self, request:Response):
        user_id = request.query_params['user_id']
        try:
            instance = Account.objects.get(id = user_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "User status changed"}, status=status.HTTP_200_OK)
        
        except :
            return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class AllJobsGet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    
    queryset = Job.objects.all()
    serializer_class = JobSerializerGet


class BlockUnBlockJobsView(APIView):
    # permission_classes = [IsAdminUser]

    def post(self, request:Response):
        job_id = request.query_params['job_id']
        try:
            instance = Job.objects.get(id = job_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "Job status changed"}, status=status.HTTP_200_OK)
        
        except :
            return Response({"message": "Job not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class NotificationCountView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request:Response):
        count = Notifications.objects.filter(is_admin=True, is_seen=False).count()
        return Response(data={'count':count}, status=status.HTTP_200_OK)
    

class NotificationsView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request:Response):
        instances = Notifications.objects.filter(is_admin=True).order_by('-created_at')
        serializer = NotificationSerializer(instance=instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class NotificaionSeenView(APIView):
    # permission_classes = [IsAdminUser]
    
    def patch(self, request:Response):

        instances = Notifications.objects.filter(is_admin=True, is_seen=False)

        for instance in instances:
            instance.is_seen = True
            instance.save()
        
        return Response({"message" : "Notification updated"}, status=status.HTTP_200_OK)
    

class QuaificationPostView(APIView):
    # permission_classes = [IsAdminUser]

    def post(self, request:Response):
        serializer = QualificationSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New Qualification added successfully"}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"message": "Qualification adding failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class QualificationsUpdateView(APIView):

    # permission_classes = [IsAdminUser]

    def patch(self, request:Response):
        q_id = request.query_params['q_id']
        try:
            instance = Qualification.objects.get(id=q_id)
            serializer = QualificationSerializer(instance=instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Qualification updated successfully"}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response({"message": "Qualification updation failed"}, status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response({"message": "Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class QualificationsDeleteView(APIView):

    # permission_classes = [IsAdminUser]

    def get(self, request:Response):
        q_id = request.query_params['q_id']
        try:
            instance = Qualification.objects.get(id=q_id)
            instance.delete()
            return Response({"message": "Qualification updated successfully"}, status=status.HTTP_200_OK)
            
        except:
            return Response({"message": "Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class SingleQualificationView(APIView):

    # permission_classes = [IsAdminUser]

    def get(self, request:Response):
        q_id = request.query_params['q_id']
        try:
            instance = Qualification.objects.get(id=q_id)
            serializer = QualificationSerializer(instance=instance)
            return Response(data=serializer.data , status=status.HTTP_200_OK)
            
        except:
            return Response({"message": "Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        


class PaymentDetailsView(ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailSerializer



class DashboradView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request:Response):
        recuiter_count = Company.objects.all().count()
        seeker_count = SeekerProfile.objects.all().count()
        job_count = Job.objects.all().count()
        subsciption_count = PaymentDetails.objects.all().count()
        total_earnings = PaymentDetails.objects.aggregate(Sum('amount_paid'))['amount_paid__sum']

        data = {
            'recuiter_count' : recuiter_count,
            'seeker_count' : seeker_count,
            'job_count' : job_count,
            'subsciption_count' : subsciption_count,
            'total_earnings' : total_earnings
            
        }

        return Response(data=data, status=status.HTTP_200_OK)

        





