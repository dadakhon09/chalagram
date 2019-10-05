from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='', )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def wtf(sender, instance, created, **kwargs):
    if created:
        room_name = instance.username
        if UserProfile.objects.filter(room_name=room_name).exists():
            pass
        else:
            up = UserProfile(user=instance, room_name=room_name)
            up.save()


class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'rooms'

    def __str__(self):
        return self.room_name


class Message(models.Model):
    message = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'messages'

    def __str__(self):
        return self.message


class UserRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        db_table = 'user_rooms'
