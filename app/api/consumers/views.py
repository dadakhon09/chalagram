from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from app.api.consumers.serializers import MessageSerializer
from app.models import Message


class MessagesList(ListAPIView):
    lookup_field = 'room_name'
    serializer_class = MessageSerializer

    def get_queryset(self):
        Message.objects.filter(room=self.kwargs['room_name'])
