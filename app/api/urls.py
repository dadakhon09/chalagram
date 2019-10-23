from django.urls import path

from app.api.consumers.views import MessagesList, CreateRoom, MessageUpdate, MessageDelete, RoomUpdate, RoomDelete, \
    RoomsList, MyRoomsList
from app.api.users.views import UserRegister, UserLogin, UserLogout, UserListAll, FriendsList, \
    AddFriend, EditPhoto, UserDelete, UserDetail, UserUpdate

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),

    path('users/list/', UserListAll.as_view(), name='users-list'),  # not really needed
    path('users/list/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
    path('users/list/<int:id>/update/', UserUpdate.as_view(), name='user-update'),
    path('users/list/<int:user_id>/editphoto/', EditPhoto.as_view(), name='user-editphoto'),
    path('users/list/<int:user_id>/delete/', UserDelete.as_view(), name='user-delete'),
    path('friends/list/', FriendsList.as_view(), name='friend-list'),
    path('add/friend/', AddFriend.as_view(), name='add-friend'),

    path('messages/list/<int:id>/update/', MessageUpdate.as_view(), name='message-update'),
    path('messages/list/<int:id>/delete/', MessageDelete.as_view(), name='message-delete'),
    path('messages/list/<str:room_name>/', MessagesList.as_view(), name='messages-list'),
    path('create-room/', CreateRoom.as_view(), name='create-room'),
    path('rooms/list/', RoomsList.as_view(), name='rooms-list'),  # not really needed
    path('rooms/list/<int:id>/update/', RoomUpdate.as_view(), name='room-update'),
    path('rooms/list/<int:id>/delete/', RoomDelete.as_view(), name='room-delete'),
    path('rooms/list/my/', MyRoomsList.as_view(), name='my-rooms-list'),
]
