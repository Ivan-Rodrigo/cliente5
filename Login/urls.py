from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls import url, re_path


from Login.views import CustonAuthToken


urlpatterns = [
    re_path(r'^', CustonAuthToken.as_view()),
]