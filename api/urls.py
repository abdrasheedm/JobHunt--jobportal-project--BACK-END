from django.urls import path,include
from rest_framework import routers
from superuser.views import CompanyCategoryView, CompanyDepartmentView
from recruiter.views import (CompanyView, CompanyUpdateView, UpdateView, PostJobView, JobView, SingleJobView, JobUpdateView, JobDeleteView, QualificationsView,
                             MembershipPurchaseView,PlanDetailsView, ApplicationTrackingView, ApplicantShortlisiView, ShortlistedApplicantView, RemoveShortlistedCandidateView)
from seeker.views import (SeekerProfileView, SeekerProfileUpdateView, PostEducationView, UpdateEducationView, SeekerEducationView, 
                          SeekerExperienceSingleView, PostExperienceView, UpdateExperienceView, SeekerExperienceView,
                          SeekerProjectView, SeekerProjectSingleView, PostProjectView, UpdateProjectView, BrowseJobsView, ApplyJobView, 
                          FavouriteJobView, FavouriteJobGetView, RemoveFavouritedJobView, FavouriteJobListView, AppliedJobsView, AppliedJobRemoveView
                          , DeleteExperienceView, DeleteProjectView, AllSeekersGetView, ReportJobView, ReportedJobsView)

from home.views import TopJobsView
from notifications.views import NotificatinView, UnreadNotificationCountView, UpdateNotificationView
from superuser.views import (AllUserGet, BlockUnBlockUserView, AllJobsGet, BlockUnBlockJobsView, CategoryAddView, CategorUpdateView, CategoryRemoveView, SingleCategoryView,
                             AllDepartmentView, AddDepartmentView, UpdateDepartmentView, SingleDepartmentView, RemoveDepartmentView, NotificationCountView, NotificationsView,
                             NotificaionSeenView, QualificationsUpdateView, QuaificationPostView, QualificationsDeleteView, SingleQualificationView, PaymentDetailsView, DashboradView)




# from .views import MeView


router = routers.DefaultRouter()
router.register(r'company-category', CompanyCategoryView, basename='view-company-category')
router.register(r'all-user', AllUserGet, basename='view-all-users')
router.register(r'all-jobs', AllJobsGet, basename='view-all-jobs')
router.register(r'all-departments', AllDepartmentView, basename='view-all-departments')
router.register(r'subsciption-details', PaymentDetailsView, basename='view-all-subsciptions')
router.register(r'reported-jobs', ReportedJobsView, basename='view-reported-jobs')


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


    path('notifications/', NotificatinView.as_view(), name='notifications'),
    path('notifications-count-view/', UnreadNotificationCountView.as_view(), name='notifications-count'),
    path('notifications-update-view/', UpdateNotificationView.as_view(), name='notifications-update'),

    path('job-qualifications-view/', QualificationsView.as_view(), name='view-job-qualifications'),
    path('membership-purchase-view/', MembershipPurchaseView.as_view(), name='membership-purchase-view'),
    path('plan-details-view/', PlanDetailsView.as_view(), name='plan-details-view'),

    path('applicaion-tracking/', ApplicationTrackingView.as_view(), name='application-tracking-view'),
    path('applicant-shortlist/', ApplicantShortlisiView.as_view(), name='applicant-shortlist-view'),
    path('shortlisted-applicant/', ShortlistedApplicantView.as_view(), name='shortlisted-applicant-view'),
    path('delete-shortlisted-applicant/', RemoveShortlistedCandidateView.as_view(), name='delete-applicant-view'),



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
    path('report-jobs/', ReportJobView.as_view(), name='report-jobs'),






    # Admin
    path('user-block-unblock-view/', BlockUnBlockUserView.as_view(), name='user-block-unblock'),
    path('job-block-unblock-view/', BlockUnBlockJobsView.as_view(), name='job-block-unblock'),
    #Category Management
    path('add-category-view/', CategoryAddView.as_view(), name='add-category'),
    path('update-category-view/', CategorUpdateView.as_view(), name='update-category'),
    path('remove-category-view/', CategoryRemoveView.as_view(), name='remove-category'),
    path('single-category-view/', SingleCategoryView.as_view(), name='single-category'),

    # department Management
    
    path('add-department-view/', AddDepartmentView.as_view(), name='add-department'),
    path('update-department-view/', UpdateDepartmentView.as_view(), name='update-department'),
    path('remove-department-view/', RemoveDepartmentView.as_view(), name='remove-department'),
    path('single-department-view/', SingleDepartmentView.as_view(), name='single-department'),


    #Admin Notifications
    path('notification-count/', NotificationCountView.as_view(), name='notification-count'),
    path('admin-notifications/', NotificationsView.as_view(), name='notification-view'),
    path('admin-notifications-seen-view/', NotificaionSeenView.as_view(), name='notification-seen-view'),



    # Qualification Management
    
    path('add-qualification-view/', QuaificationPostView.as_view(), name='add-qualifcation'),
    path('update-qualifcation-view/', QualificationsUpdateView.as_view(), name='update-qualifcation'),
    path('remove-qualifcation-view/', QualificationsDeleteView.as_view(), name='remove-qualifcation'),
    path('single-qualifcation-view/', SingleQualificationView.as_view(), name='single-qualifcation'),

    # Dashboard
    path('dashboard-view/', DashboradView.as_view(), name='dahsboard-view'),


    #Home 
    path('top-job-view/', TopJobsView.as_view(), name='top-job-view'),








]
urlpatterns += router.urls

