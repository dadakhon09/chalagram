from django.urls import path

from chat.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
