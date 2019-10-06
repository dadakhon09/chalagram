from django.contrib import admin

from app.models import Room, Message, UserRoom, UserProfile, Friendship

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(UserRoom)
admin.site.register(UserProfile)
admin.site.register(Friendship)
