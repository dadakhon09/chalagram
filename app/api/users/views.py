from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.users.serializers import UserProfileSerializer, FriendshipSerializer, FriendshipCreateSerializer, \
    UserProfilePhotoSerializer, UserSerializer
from app.models import UserProfile, Friendship


@permission_classes((AllowAny,))
class UserRegister(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username=username, password=password)
            token, _ = Token.objects.get_or_create(user=new_user)
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password!'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials!'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id': user.id,
                         'username': user.username,
                         })


class UserLogout(APIView):
    def get(self, request):
        if request.user:
            request.user.auth_token.delete()
        else:
            Response("Please login first")
        return Response("Successfully logged out")


class UserListAll(ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class EditPhoto(RetrieveUpdateAPIView):
    lookup_field = 'user_id'
    serializer_class = UserProfilePhotoSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user__id=self.kwargs['user_id'])


class UserUpdate(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['id'])


class UserDelete(RetrieveDestroyAPIView):
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user__id=self.kwargs['user_id'])


class UserDetail(RetrieveAPIView):
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user__id=self.kwargs['user_id'])


class FriendsList(ListAPIView):
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        return Friendship.objects.filter(userprofile__user_id=self.request.user.id)


class AddFriend(CreateAPIView):
    serializer_class = FriendshipCreateSerializer
