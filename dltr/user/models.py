from datetime import date

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class User(models.Model):

    """用户
    字段按照Char, Text, Date, Time, Integer, Boolean排序"""

    uid = models.CharField(primary_key=True, max_length=50)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)  # 用户密码的md5值
    portrait = models.CharField(max_length=50, default="e2c1776c31393837313031319605")  # 默认头像

    info = models.JSONField()
    brief = RichTextField()

    sign_in_date = models.DateField()

    fans = models.PositiveIntegerField(default=0)
    words = models.PositiveIntegerField(default=0)
    fictions = models.PositiveIntegerField(default=0)

    is_writer = models.BooleanField()
    is_male = models.BooleanField()
    can_rename = models.BooleanField(default=True)

    def __str__(self):
        return "user_{}".format(self.uid)

    def get_small_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portraitn/item/{}".format(self.portrait)

    def get_large_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portrait/item/{}".format(self.portrait)
