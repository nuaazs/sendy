from django.db import models
import time
# Create your models here.
class Logs(models.Model):
    consumer = models.CharField('刷手旺旺号',max_length=256)
    send_time = models.DateTimeField('发单时间',default = time.time())
    done_time = models.DateTimeField('完成时间或打回时间',default = time.time())
    sender = models.CharField('发单人',max_length=256)
    pic_url = models.CharField('主图链接',max_length=256)
    uuid = models.CharField('识别码',max_length=256)
    isback = models.IntegerField('是否打回')
    isdone = models.IntegerField('是否完成')