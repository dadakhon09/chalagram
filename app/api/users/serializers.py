from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.models import UserProfile, Friendship


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'photo')


class FriendshipSerializer(ModelSerializer):
    userprofile = UserProfileSerializer()
    friends = UserProfileSerializer()

    class Meta:
        model = Friendship
        fields = ('userprofile', 'friends')
