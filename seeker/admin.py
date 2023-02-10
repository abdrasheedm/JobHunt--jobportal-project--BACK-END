from django.contrib import admin
from .models import SeekerProfile, Education, Experience, Projects, AppliedJobs

# Register your models here.

admin.site.register(SeekerProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(AppliedJobs)
