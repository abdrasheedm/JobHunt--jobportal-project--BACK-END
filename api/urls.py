from django.urls import path,include
from rest_framework import routers
from superuser.views import CompanyCategoryView, CompanyDepartmentView
from recruiter.views import CompanyView, CompanyUpdateView, UpdateView, PostJobView, JobView, SingleJobView, JobUpdateView, JobDeleteView, QualificationsView
from seeker.views import (SeekerProfileView, SeekerProfileUpdateView, PostEducationView, UpdateEducationView, SeekerEducationView, 
                          SeekerExperienceSingleView, PostExperienceView, UpdateExperienceView, SeekerExperienceView,
                          SeekerProjectView, SeekerProjectSingleView, PostProjectView, UpdateProjectView, BrowseJobsView, ApplyJobView, 
                          FavouriteJobView, FavouriteJobGetView, RemoveFavouritedJobView, FavouriteJobListView, AppliedJobsView, AppliedJobRemoveView
                          , DeleteExperienceView, DeleteProjectView, AllSeekersGetView)

# from .views import MeView


router = routers.DefaultRouter()
router.register(r'company-category', CompanyCategoryView, basename='view-company-category')


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
    path('all-seekers-profile/', AllSeekersGetView.as_view(), name='view-all-seeker-profile'),

    path('job-qualifications-view/', QualificationsView.as_view(), name='view-job-qualifications'),



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
    path('delete-seeker-experience/', DeleteExperienceView.as_view(), name='delete-seeker-experience'),

    # Project
    path('seeker-project-single/', SeekerProjectSingleView.as_view(), name='view-seeker-single-project'),
    path('seeker-project/', SeekerProjectView.as_view(), name='view-seeker-project'),
    path('post-seeker-project/', PostProjectView.as_view(), name='post-seeker-project'),
    path('update-seeker-project/', UpdateProjectView.as_view(), name='update-seeker-project'),
    path('delete-seeker-project/', DeleteProjectView.as_view(), name='delete-seeker-project'),


    path('browse-job/', BrowseJobsView.as_view(), name='browse-job'),

    path('apply-job/', ApplyJobView.as_view(), name='apply-job'),
    path('applied-jobs/', AppliedJobsView.as_view(), name='applied-jobs-view'),
    path('remove-applied-job/', AppliedJobRemoveView.as_view(), name='applied-jobs-remove'),
    
    path('favourite-job/', FavouriteJobView.as_view(), name='addandremove-from-favourites'),
    path('seeker-favourited-job/', FavouriteJobGetView.as_view(), name='favourite-job-get'),
    path('seeker-remove-favourited-job/', RemoveFavouritedJobView.as_view(), name='favourite-job-remove'),
    path('favourite-job-list/', FavouriteJobListView.as_view(), name='list-favourite-jobs'),





]
urlpatterns += router.urls

