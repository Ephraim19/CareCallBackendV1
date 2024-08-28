from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chats/', consumers.YourConsumer.as_asgi()),
]