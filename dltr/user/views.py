from django.shortcuts import render
from django.http import HttpResponseNotFound

from . import models


# Create your views here.


def callback(request):
    pass


def sign_in(request):
    return render(request, "signin.html")


def user_home(request, uuid):
    user = models.User.objects.get(uuid__exact=uuid)
    if user:
        return render(request, 'user_home.html', {
            'name': user.user_name,
        })
    else:
        return HttpResponseNotFound()
