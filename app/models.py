from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profile-pictures.png', upload_to='', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def wtf(sender, instance, created, **kwargs):
    if created:
        up = UserProfile(user=instance)
        up.save()


class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    room_uid = models.CharField(max_length=127, unique=True, null=True, blank=True)
    userprofiles = models.ManyToManyField(UserProfile, related_name='userprofiles')
    created = models.DateTimeField(auto_now_add=True)

    def get_usernames(self):
        return [u.user.username for u in self.userprofiles.all()]

    class Meta:
        ordering = ['id']
        db_table = 'rooms'

    def __str__(self):
        return self.room_name


class Message(models.Model):
    message = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    # receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'messages'

    def __str__(self):
        return self.message


class File(models.Model):
    file = models.FileField(upload_to='', blank=True, null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'files'

    def __str__(self):
        return self.file.name

# class UserRoom(models.Model):
#     userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_rooms'
#
#     def __str__(self):
#         return self.room_name.room_name


class Friendship(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    friend = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friend')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'friendship'

    def __str__(self):
        return f'{self.userprofile}<->{self.friend}'
