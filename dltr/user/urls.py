from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^signin\.html/$', views.sign_in, name="signin"),         # 注册
    url(r'^callback\.html/$', views.callback, name="callback"),    # 百度回调页面
    path('rename.html', views.rename, name="rename"),              # 重命名
    url(r'^(.+)\.html/$', views.user_home, name="user_home"),      # 用户主页
]
