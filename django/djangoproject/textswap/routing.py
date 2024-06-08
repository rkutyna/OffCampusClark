from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/messaging/(?P<recipient_username>\w+)/$', consumers.ChatConsumer.as_asgi()),
    path('ws/inbox/', consumers.InboxConsumer.as_asgi()),
]

