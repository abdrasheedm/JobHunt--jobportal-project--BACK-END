from django.urls import path,include
from rest_framework import routers
from superuser.views import CompanyCategoryView, CompanyDepartmentView
from recruiter.views import CompanyView, CompanyUpdateView, UpdateView, PostJobView, JobView, SingleJobView, JobUpdateView, JobDeleteView
from seeker.views import (SeekerProfileView, SeekerProfileUpdateView, PostEducationView, UpdateEducationView, SeekerEducationView, 
                          SeekerExperienceSingleView, PostExperienceView, UpdateExperienceView, SeekerExperienceView,
                          SeekerProjectView, SeekerProjectSingleView, PostProjectView, UpdateProjectView, BrowseJobsView, ApplyJobView)

# from .views import MeView


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
    path('view-single-job/', SingleJobView.as_view(), name='job-view'),
    path('recruiter-delete-job/', JobDeleteView.as_view(), name='job-delete'),

    path('seeker-profile/', SeekerProfileView.as_view(), name='view-seeker-profile'),
    path('update-seeker-profile/', SeekerProfileUpdateView.as_view(), name='update-seeker-profile'),

    path('seeker-education/', SeekerEducationView.as_view(), name='view-seeker-education'),
    path('post-seeker-education/', PostEducationView.as_view(), name='post-seeker-education'),
    path('update-seeker-education/', UpdateEducationView.as_view(), name='update-seeker-education'),

    # Experience 
    path('seeker-experience-single/', SeekerExperienceSingleView.as_view(), name='view-seeker-single-experience'),
    path('seeker-experience/', SeekerExperienceView.as_view(), name='view-seeker-experience'),
    path('post-seeker-experience/', PostExperienceView.as_view(), name='post-seeker-experience'),
    path('update-seeker-experience/', UpdateExperienceView.as_view(), name='update-seeker-experience'),

    # Project
    path('seeker-project-single/', SeekerProjectSingleView.as_view(), name='view-seeker-single-project'),
    path('seeker-project/', SeekerProjectView.as_view(), name='view-seeker-project'),
    path('post-seeker-project/', PostProjectView.as_view(), name='post-seeker-project'),
    path('update-seeker-project/', UpdateProjectView.as_view(), name='update-seeker-project'),


    path('browse-job/', BrowseJobsView.as_view(), name='browse-job-view'),
    path('apply-job/', ApplyJobView.as_view(), name='apply-job-view'),




]
urlpatterns += router.urls

