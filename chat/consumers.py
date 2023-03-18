from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )

    def receive(self, text_data=None, bytes_data=None):
        pass

    async def disconnect(self, code):
        pass