"""
ASGI config for nimbus project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nimbus.settings')

application = get_asgi_application()

ws_pattern = [
    #print("hello"),
    path('chat/<room_code>', ChatConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket': (URLRouter(ws_pattern))
})
