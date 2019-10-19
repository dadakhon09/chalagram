from django.core.serializers import serialize
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.consumers.serializers import MessageSerializer, MessageUpdateSerializer, RoomUpdateSerializer, \
    RoomSerializer
from app.api.users.serializers import UserProfileSerializer
from app.models import Message, Room, UserProfile


class MessagesList(ListAPIView):
    lookup_field = 'room_name'
    serializer_class = MessageSerializer

    def get_queryset(self):
        room = Room.objects.get(room_name=self.kwargs['room_name'])
        return Message.objects.filter(room=room)


class RoomsList(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class MyRoomsList(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        qs = Room.objects.all()
        user = self.request.user

        list = Room.objects.filter(id=-1)

        for room in qs:
            for u in room.get_usernames():
                if u == user.username:
                    list |= Room.objects.filter(room_name=room.room_name)
        return list


class CreateRoom(APIView):
    def post(self, request):
        data = request.data

        userprofiles_list = UserProfile.objects.filter(id=-1)

        users = self.request.POST.getlist('user')
        room_name = self.request.POST.get('room_name')
        room = Room(room_name=room_name)
        room.save()

        for u in users:
            userprofiles_list |= UserProfile.objects.filter(user__username=u)
            room.userprofiles.add(UserProfile.objects.filter(user__username=u).first())
            room.save()
        userprofiles_list |= UserProfile.objects.filter(user__username=self.request.user.username)
        ser = UserProfileSerializer(userprofiles_list, many=True)

        response = {'users': ser.data, 'room_name': room_name}

        return Response(response)


class MessageUpdate(RetrieveUpdateAPIView):
    serializer_class = MessageUpdateSerializer
    lookup_field = 'id'
    queryset = Message.objects.all()


class MessageDelete(RetrieveDestroyAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'id'
    queryset = Message.objects.all()


class RoomUpdate(RetrieveUpdateAPIView):
    serializer_class = RoomUpdateSerializer
    lookup_field = 'id'
    queryset = Room.objects.all()


class RoomDelete(RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    lookup_field = 'id'
    queryset = Room.objects.all()

