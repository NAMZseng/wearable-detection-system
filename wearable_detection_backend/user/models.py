from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name='昵称', max_length=32, default='User')
    phone = models.CharField(verbose_name='电话号码', max_length=12)
    password = models.CharField(verbose_name='登录密码', max_length=40)
    sex = models.CharField(verbose_name='性别', max_length=10, choices=(('male', '男'), ('female', '女')))
    birthday = models.DateField(verbose_name='出生日期')
