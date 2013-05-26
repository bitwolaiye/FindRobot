# encoding:utf8

from django.db import models

# Create your models here.


class WeiboUser(models.Model):
    weibo_uid = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    small_avatar = models.CharField(max_length=100)
    user_desc = models.CharField(max_length=500, null=True)
    gender = models.PositiveSmallIntegerField(default=0)
    getcai_uid = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'weibo_user'


class PicWeibo(models.Model):
    weibo_user = models.ForeignKey(WeiboUser)
    pic_url = models.CharField(max_length=200)
    weibo_text = models.CharField(max_length=500, null=True)
    selected = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'pic_weibo'


class PicAvatar(models.Model):
    weibo_user = models.ForeignKey(WeiboUser)
    pic_url = models.CharField(max_length=200)
    selected = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'pic_avatar'

