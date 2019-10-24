from rest_framework.serializers import ModelSerializer

from app.models import Message, Room, File


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'room', 'sender', 'created')


class MessageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message')


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_name', 'userprofiles')


class RoomUpdateSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_name')


class FilesSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('file', )
