from asyncio import SendfileNotAvailableError
from statistics import mode
from tabnanny import verbose
from django.db import models
import time

# Create your models here.


class Stores(models.Model):
    full_name = models.CharField('店铺全称',max_length=128,unique=True,editable=True)
    short_name = models.CharField('店铺缩写',max_length=16,unique=True,editable=True)
    limit = models.IntegerField('每小时上限',editable=True)
    remain = models.IntegerField('剩余可发送量',editable=True)
    changed_time = models.DateTimeField('保存日期',default = time.time())
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "店铺信息"
        verbose_name_plural = "所有店铺信息"

# 新建数据
# UserInfo.objects.create(name="赵胜",password="zhaosheng",age=18)