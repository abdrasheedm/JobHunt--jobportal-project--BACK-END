from django.urls import path,include
from rest_framework import routers
from superuser.views import CompanyCategoryView, CompanyDepartmentView
from recruiter.views import CompanyView, CompanyUpdateView, UpdateView, PostJobView, JobView, SingleJobView, JobUpdateView, JobDeleteView


router = routers.DefaultRouter()
router.register(r'company-category', CompanyCategoryView, basename='view-company-category')
# router.register(r'recruiter-view-job/', JobView, basename='view-jobs')
# router.register(r'company-department', CompanyDepartmentView, basename='view-company-department')
# router.register(r'company-profile', CompanyView, basename='view-company-profile')

urlpatterns = [
    path('user/', include('accounts.urls')),
    path('company-profile/', CompanyView.as_view(), name='view-company-profile'),
    path('update-company-profile/', CompanyUpdateView.as_view(), name='update-company-profile'),
    path('update/', UpdateView.as_view(), name='update'),
    path('company-department/', CompanyDepartmentView.as_view(), name='view-company-department'),
    path('recruiter-post-job/', PostJobView.as_view(), name='job-post'),
    path('recruiter-update-job/', JobUpdateView.as_view(), name='job-update'),
    path('recruiter-view-job/', JobView.as_view(), name='job-view'),
    path('recruiter-view-single-job/', SingleJobView.as_view(), name='job-view'),
    path('recruiter-delete-job/', JobDeleteView.as_view(), name='job-delete'),


]
urlpatterns += router.urls

