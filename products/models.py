from django.db import models
import time
# Create your models here.

class Products(models.Model):
    product_id = models.CharField('商品ID',max_length=32)
    word_index = models.IntegerField('关键词序号')
    total = models.IntegerField('该款该词总单量')
    remain = models.IntegerField('该款该词剩余量')
    remain = models.IntegerField('该款该词剩余量')
    isactive = models.IntegerField('是否激活')
    date = models.DateTimeField('计划发单日期',default = time.time())
    uuid = models.CharField('识别码',max_length=256)

class Words(models.Model):
    uuid = models.CharField('识别码',max_length=256)
    word = models.CharField('关键词',max_length=256)

class Pictures(models.Model):
    uuid = models.CharField('识别码',max_length=256)
    pic_url = models.CharField('主图链接',max_length=256)

class Priority(models.Model):
    product_id = models.CharField('商品ID',max_length=32)
    priority = models.IntegerField('优先级')

class Numbers(models.Model):
    uuid = models.CharField('识别码',max_length=256)
    number = models.CharField('件数',max_length=256)

class Messages(models.Model):
    uuid = models.CharField('识别码',max_length=256)
    message = models.CharField('备注信息',max_length=256)