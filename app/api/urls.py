from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from app.api.users.views import UserRegister, UserLogin, UserLogout, UserListAll, UserListExceptOne

schema_view = get_swagger_view(title='Documentation')


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),

    path('users/list/', UserListAll.as_view(), name='users-list'),
    path('users/my/', UserListExceptOne.as_view(), name='users-my'),
]
