from django.urls import path

from app.api.users.views import UserRegister, UserLogin, UserLogout, UserListAll, UserListExceptOne, FriendsList

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),

    path('users/list/', UserListAll.as_view(), name='users-list'),
    path('users/my/', UserListExceptOne.as_view(), name='users-my'),
    path('users/friends/', FriendsList.as_view(), name='friend-list'),
]
