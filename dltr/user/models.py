from django.db import models

# Create your models here.


class User(models.Model):
    """用户"""
    uid = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20)
    portrait = models.CharField(max_length=50, default="e2c1776c31393837313031319605")  # 默认头像
    password = models.CharField(max_length=30, default="password")      # 以用户密码的md5值作为原值，以id作为哈希盐值
    access_token = models.CharField(max_length=100, default="")
    refresh_token = models.CharField(max_length=100, default="")

    def get_small_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portraitn/item/{}".format(self.portrait)

    def get_large_face_image_url(self):
        return "http://tb.himg.baidu.com/sys/portrait/item/{}".format(self.portrait)
