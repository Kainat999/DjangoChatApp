from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:groupname>/', consumers.chatConsumer.as_asgi()),
    path('ws/AsyncChat/<str:groupname>/', consumers.chatAsyncConsumer.as_asgi()),
]