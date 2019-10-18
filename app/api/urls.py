from django.urls import path

from app.api.consumers.views import MessagesList, CreateRoom, MessageUpdate, MessageDelete, RoomUpdate, RoomDelete, \
    RoomsList, ChatList
from app.api.users.views import UserRegister, UserLogin, UserLogout, UserListAll, UserListExceptOne, FriendsList, \
    AddFriend

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),

    path('users/list/', UserListAll.as_view(), name='users-list'),
    path('users/my/', UserListExceptOne.as_view(), name='users-my'),
    path('friends/list/', FriendsList.as_view(), name='friend-list'),
    path('add/friend/', AddFriend.as_view(), name='add-friend'),
    path('messages/list/<str:room_name>/', MessagesList.as_view(), name='messages-list'),
    path('messages/list/<int:id>/update/', MessageUpdate.as_view(), name='message-update'),
    path('messages/list/<int:id>/delete/', MessageDelete.as_view(), name='message-delete'),
    path('create-room/', CreateRoom.as_view(), name='create-room'),
    path('rooms/list/', RoomsList.as_view(), name='rooms-list'),
    path('rooms/list/<int:id>/update/', RoomUpdate.as_view(), name='room-update'),
    path('rooms/list/<int:id>/delete/', RoomDelete.as_view(), name='room-delete'),
    path('chat/list/my/', ChatList.as_view(), name='my-chat-list'),
]
