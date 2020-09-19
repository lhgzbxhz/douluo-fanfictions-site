from urllib.parse import quote
from datetime import date
from hashlib import md5

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect

from user import models
from user.forms import UserForm
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
        try:
            user = models.User.objects.get(uid__exact=info["openid"])
            return redirect("user_home", user.uid)
        except models.User.DoesNotExist:
            pass

        if request.method == 'POST':
            # 初始化表单
            form = UserForm(request.POST)
            # 初始化模型
            user = form.save(commit=False)
            user.uid = info.pop("openid")
            user.password = md5(user.password.encode()).hexdigest()
            user.portrait = info.pop("portrait")
            user.info = info

            user.is_male = bool(int(info.pop("sex")))
            user.is_writer = (request.POST["user-type"] == '作者')

            user.sign_in_date = date.today()
            user.save()
            # 存入session
            request.session["uid"] = user.uid
            # 重定向
            return redirect(reverse("user_home", args=(user.uid,)))

        else:
            form = UserForm()
            return render(request, "signin.html", {
                'name': info["username"],
                'form': form,
            })
    else:
        return redirect(get_authorization_code_url(
            callback_uri=quote("http://127.0.0.1:8000/user/callback.html")))


def user_home(request, uid):
    user = models.User.objects.get(uid__exact=uid)
    if user:
        return render(request, 'user_home.html', {
            'user': user,
        })
    else:
        return HttpResponseNotFound()


def rename(request):
    uid = request.session.get("uid")
    if not uid:
        return HttpResponseNotFound("您尚未登录！".encode())

    if request.method == 'POST':
        user = models.User.objects.get(uid__exact=uid)
        user.uname = request.POST["new_name"]
        user.can_rename = False
        user.save()
        return redirect('user_home', uid)

    else:
        return render(request, "rename.html", {
            'can_rename': models.User.objects.get(uid__exact=uid).can_rename,
        })
