from django.db import models

# Create your models here.


class User(models.Model):
    uuid = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    photo_url = models.URLField()

    class Meta:
        ordering = ['uuid']
