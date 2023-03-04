from django.urls import path,include
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('verify-otp/', views.Verify_otpView.as_view(), name='verify_otp'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
