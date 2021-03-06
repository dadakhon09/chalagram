from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.contrib.auth.models import User
from rest_framework.response import Response

from app.api.consumers.serializers import FilesSerializer
from app.models import Message, Room, File


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json.get('message')

        if text_data_json.get('sender'):
            s = text_data_json.get('sender')
        else:
            return Response('Sorry, who is sending that?')

        # r = text_data_json['receiver']

        sender = User.objects.get(username=s)
        # receiver = User.objects.get(id=r)

        room, _ = Room.objects.get_or_create(room_name=self.room_name)
        # user_room, _ = UserRoom.objects.get_or_create(userprofile=sender.userprofile, room_name=room)
        m = Message.objects.create(message=message, room=room, sender=sender)

        files = File.objects.filter(id=-1)
        ser = FilesSerializer(files)

        if text_data_json.get('files'):
            for f in text_data_json.get('files'):
                file = File.objects.create(file=f, message=m)
                files |= file
                ser = FilesSerializer(files, many=True)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                # 'receiver': receiver.username,
                'room_name': self.room_name,
                'files': ser.data,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        # receiver = event['receiver']
        room_name = event['room_name']
        files = event['files']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            # 'receiver': receiver,
            'room_name': room_name,
            'files': files,
        }))
