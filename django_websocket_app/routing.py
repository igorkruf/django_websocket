# Пример routing.py для приложения 
from django.urls import re_path, path 
from .consumers import MyConsumer 
 
websocket_urlpatterns = [ 
    path('ws/', MyConsumer.as_asgi()), 
]