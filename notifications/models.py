from django.db import models
from accounts.models import Account

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your models here.
class Notifications(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)

    def save(self,*args, **kwargs):
        channel_layer = get_channel_layer()
        notification_objs = Notifications.objects.filter(is_seen=False).count()
        data = {'count' : notification_objs, 'notification' : self.notification}

        async_to_sync(channel_layer.group_send)(
            'notification_'+str(self.user.id), {
            'type' : 'sent_notification',
            'value' : json.dumps(data)
            }
        )

        super(Notifications, self).save(*args, **kwargs)

    def __str__(self):
        return self.notification