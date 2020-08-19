from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.user_home),
]
