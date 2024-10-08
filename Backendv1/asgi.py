"""
ASGI config for Backendv1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import BioData.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backendv1.settings')

application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            BioData.routing.websocket_urlpatterns
        )
    ),
})

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import Biodata.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backendv1.settings')

