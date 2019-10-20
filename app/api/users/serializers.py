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


class UserProfilePhotoSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('photo', )
    #
    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     # username = validated_data.pop('username')
    #     # photo = validated_data.pop('photo')
    #     # instance.user.username = username
    #     # instance.photo = photo
    #     # instance.save()
    #     return instance


class FriendshipSerializer(ModelSerializer):
    # userprofile = UserProfileSerializer()
    friends = UserProfileSerializer()

    class Meta:
        model = Friendship
        fields = ('friend', )


class FriendshipCreateSerializer(ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('friend', )

    def create(self, validated_data):
        f = Friendship.objects.create(userprofile=self.context['request'].user.userprofile, **validated_data)
        return f