from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/whatsapp/', consumers.YourConsumer.as_asgi()),
]