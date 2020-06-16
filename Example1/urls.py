from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls import url, re_path


from Example1 import views

urlpatterns = [
    re_path(r'/example1/$', views.ExampleList.as_view()),
]
