from django.contrib import admin
from .models import SeekerProfile, Education, Experience, Projects, AppliedJobs, FavouriteJob, ReportJob

# Register your models here.

admin.site.register(SeekerProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(AppliedJobs)
admin.site.register(FavouriteJob)
admin.site.register(ReportJob)

