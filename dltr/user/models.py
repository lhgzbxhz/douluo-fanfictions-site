from django.db import models

# Create your models here.


class Token(models.Model):
    """用户百度token"""
    access_token = models.CharField(primary_key=True, max_length=100)
    refresh_token = models.CharField(max_length=100)
    expires_in = models.PositiveIntegerField()
    scope = models.CharField(max_length=50)
    session_key = models.CharField(max_length=50)
    session_secret = models.CharField(max_length=50)


class User(models.Model):
    """用户"""
    uid = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20)
    portrait = models.CharField(max_length=50, default="e2c1776c31393837313031319605")  # 默认头像

    def get_small_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portraitn/item/{}".format(self.portrait)

    def get_large_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portrait/item/{}".format(self.portrait)
