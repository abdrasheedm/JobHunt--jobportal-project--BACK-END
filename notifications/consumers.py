# app/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print(self.scope['url_route'])
        self.room_name = self.scope['url_route']['kwargs']['userId']
        self.room_group_name = 'notification_%s' % self.room_name
        # Join room group
        print('in connect')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    async def disconnect(self, close_code):
        # Leave room group
        print('disconnect')
        await (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # async def receive(self, text_data):
    #     # Receive message from WebSocket
    #     print('this is notification app')
    #     # text_data_json = json.loads(text_data)
    #     text = 'this is notification app'
    #     sender = 'rasheed'
    #     # Send message to room group
    #     await (self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'receive',
    #             'message': text,
    #             'sender': sender
    #         }
    #     )

    async def sent_notification(self, event):
        print('send messge')
        # Receive message from room group
        data = json.loads(event.get('value'))
        print(data)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(data))