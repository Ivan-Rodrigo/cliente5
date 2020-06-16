from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls import url, re_path


from Example2 import views

urlpatterns = [
    re_path(r'/example2/$', views.ExampleList2.as_view()),
]