from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView

from app.api.consumers.serializers import MessageSerializer
from app.models import Message, Room


class MessagesList(ListAPIView):
    lookup_field = 'room_name'
    serializer_class = MessageSerializer

    def get_queryset(self):
        room = Room.objects.get(room_name=self.kwargs['room_name'])
        return Message.objects.filter(room=room)


class CreateGroup(APIView):
    def post(self, request):
        data = request.data
        