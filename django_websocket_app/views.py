from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin
# Create your views here.
class Test(ContextMixin, View):

    def get(self, req, **kwargs):
        return render(req, 'django_web_app/websocket.html')