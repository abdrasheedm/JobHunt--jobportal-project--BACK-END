from django.urls import path,include
from rest_framework import routers
from superuser.views import CompanyCategoryView
from recruiter.views import CompanyView, CompanyUpdateView, UpdateView


router = routers.DefaultRouter()
router.register(r'company-category', CompanyCategoryView, basename='view-company-category')
# router.register(r'company-profile', CompanyView, basename='view-company-profile')

urlpatterns = [
    path('user/', include('accounts.urls')),
    path('company-profile/', CompanyView.as_view(), name='view-company-profile'),
    path('update-company-profile/', CompanyUpdateView.as_view(), name='update-company-profile'),
    path('update/', UpdateView.as_view(), name='update'),

]
urlpatterns += router.urls

 