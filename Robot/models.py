# encoding:utf8

from django.db import models

# Create your models here.


class WeiboUser(models.Model):
    username = models.CharField(max_length=100)
    small_avatar = models.CharField(max_length=100)
    user_desc = models.CharField(max_length=500, null=True)
    gender = models.PositiveSmallIntegerField(default=0)
