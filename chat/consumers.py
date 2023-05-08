import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        self.group_name = f'room_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name

        )
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            f'room_{self.room_name}',
            {
                'type': 'send_message',
                'value': json.dumps({
                    'status': 'online'
                })
            }
        )
        self.send(text_data=json.dumps({
            'type': 'tester_message',
            'tester': 'hello world'
        }
        ))

    def receive(self, text_data):
        data = json.loads(text_data)

        print(data)

        payload = {'message': data.get('message'), 'sender': data.get('sender')}
        async_to_sync(self.channel_layer.group_send)(
            f'room_{self.room_name}',
            {
                'type': 'send_message',
                'value': json.dumps(payload)
            }
        )

    def disconnect(self, code):
        pass

    def send_message(self, text_data):
        data = json.loads(text_data['value'])
        self.send(text_data=json.dumps({
            'payload': data,
        }))
