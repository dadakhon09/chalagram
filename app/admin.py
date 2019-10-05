from django.contrib import admin

from app.models import Room, Message, UserRoom, UserProfile

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(UserRoom)
admin.site.register(UserProfile)