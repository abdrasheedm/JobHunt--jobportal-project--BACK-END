from channels.routing import ProtocolTypeRouter, URLRouter
# import app.routing
from django.urls import re_path, path

from notifications.consumers import NotificationConsumer

# websocket_urlpatterns = [
#     re_path(r'^/ws/test', TextRoomConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    re_path(r'ws/notification/(?P<userId>\w+)/$', NotificationConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
})