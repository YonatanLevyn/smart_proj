import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from channels.db import database_sync_to_async

class AnalyticsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        event = text_data_json.get('event')

        if event == 'pageview':
            from .models import PageView
            url = text_data_json.get('url')
            timestamp = timezone.now()  # Get the current time

            # Save the page view data to the database
            await database_sync_to_async(PageView.objects.create)(url=url, timestamp=timestamp)
