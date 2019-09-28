from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'index.html', {})

