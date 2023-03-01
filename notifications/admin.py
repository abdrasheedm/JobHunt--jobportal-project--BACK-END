from django.contrib import admin
from .models import Notifications

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'notification', 'user','url', 'is_admin']
admin.site.register(Notifications, NotificationAdmin)



