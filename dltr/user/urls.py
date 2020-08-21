from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.user_home),                  # 用户主页
    url(r'^signin/$', views.sign_in, name="signin"),       # 注册
    url(r'^callback/$', views.callback, name="callback"),  # 百度回调页面
]
