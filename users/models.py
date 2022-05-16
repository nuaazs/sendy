from django.db import models
import time
# Create your models here.
class Users(models.Model):
    name = models.CharField('姓名',max_length=32)
    password = models.CharField('密码',max_length=64)
    age = models.IntegerField('年龄')
    isroot = models.IntegerField('是否为管理员')
    gender = models.IntegerField('性别')