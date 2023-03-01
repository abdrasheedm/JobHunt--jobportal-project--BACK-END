from django.db import models
from accounts.models import Account

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import datetime
# Create your models here.
class Notifications(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    title = models.CharField(max_length=50, default='')
    notification = models.TextField(max_length=300)
    is_seen = models.BooleanField(default=False)
    url = models.CharField(max_length=100, null=True, blank=True)
    parameter = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        print('reached notification')
        if not self.is_seen:
            print("reached after seen")
            if self.is_admin:
                channel_layer = get_channel_layer()
                count = Notifications.objects.filter(is_admin=True,is_seen=False).count() + 1
                created_at = str(self.created_at)
                print(count)
                print(created_at)
                data = {'count' : count,'created_at' : created_at , 'title' : self.title,'notification' : self.notification}

                async_to_sync(channel_layer.group_send)(
                    'notification_admin', {
                    'type' : 'sent_notification',
                    'value' : json.dumps(data)
                    }
                )
            else:
                channel_layer = get_channel_layer()
                print("im here")
                count = Notifications.objects.filter(user=self.user.id,is_seen=False).count() + 1
                created_at = str(self.created_at)
                print(count)
                print(created_at)
                data = {'count' : count,'created_at' : created_at , 'title' : self.title,'notification' : self.notification}

                async_to_sync(channel_layer.group_send)(
                    'notification_'+str(self.user.id), {
                    'type' : 'sent_notification',
                    'value' : json.dumps(data)
                    }
                )

        super(Notifications, self).save(*args, **kwargs)

    def __str__(self):
        return self.notification