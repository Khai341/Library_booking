
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat_section.routing  # Import routing from chat_section


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my.settings')

application = ProtocolTypeRouter({
    "http":  get_asgi_application(),
    "websocket": AuthMiddlewareStack(
         URLRouter(
             chat_section.routing.websocket_urlpatterns
         )
    ),
})
