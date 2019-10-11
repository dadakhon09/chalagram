import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'index.html', {'sender': mark_safe(json.dumps(self.request.user.username)),
                                              'receiver': 2})
