from urllib.parse import quote

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect

from . import models
from .util import *


# Create your views here.


def callback(request):
    authorization_code = request.GET.get("code")
    if authorization_code:
        token = get_token_dict(authorization_code)
        token = token.get("access_token")
        request.session["token"] = token
        return redirect("signin")
    else:
        return HttpResponseNotFound()


def sign_in(request):
    # 获取token
    token = request.session.get("token")
    if token:
        return render(request, "signin.html", {
            'token': token,
        })
    else:
        return redirect(get_authorization_code_url(
            callback_uri=quote("http://127.0.0.1:8000/user/callback")))


def user_home(request, uuid):
    user = models.User.objects.get(uuid__exact=uuid)
    if user:
        return render(request, 'user_home.html', {
            'name': user.user_name,
        })
    else:
        return HttpResponseNotFound()
