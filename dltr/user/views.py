from urllib.parse import quote

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect

from user import models
from user.util import *


# Create your views here.


def callback(request):
    authorization_code = request.GET.get("code")
    if authorization_code:
        token = get_token_dict(authorization_code)
        request.session["token"] = token["access_token"]
        request.session["refresh_token"] = token["refresh_token"]
        return redirect("signin")
    else:
        return HttpResponseNotFound()


def sign_in(request):
    # 获取token
    token = request.session.get("token")
    if token:
        info = get_user_info(token)

        # 用户已存在
        if models.User.objects.get(uid__exact=info["openid"]):
            return redirect("user_home", info["openid"])

        if request.method == 'POST':
            # 存入数据库
            user = models.User(password=request.POST["password"][0])
            user.uid = info["openid"]
            user.user_name = info["uname"]
            user.portrait = info["portrait"]
            user.is_writer = (request.POST["user-type"][0] == '作者')
            user.access_token = token
            user.refresh_token = request.session["refresh_token"]
            user.save()
            # 存入session
            request.session["uid"] = user.uid
            # 重定向
            return redirect(reverse("user_home", args=(user.uid, )))
        else:
            return render(request, "signin.html", {
                'name': info["uname"],
            })
    else:
        return redirect(get_authorization_code_url(
            callback_uri=quote("http://127.0.0.1:8000/user/callback")))


def user_home(request, uid):
    user = models.User.objects.get(uid__exact=uid)
    if user:
        return render(request, 'user_home.html', {
            'name': user.user_name,
        })
    else:
        return HttpResponseNotFound()
