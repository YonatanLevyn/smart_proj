from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/analytics/', consumers.AnalyticsConsumer.as_asgi()),
]
