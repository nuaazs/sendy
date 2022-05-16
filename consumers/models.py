from django.db import models
import time
# Create your models here.
class Consumers(models.Model):
    tmall_username = models.CharField('旺旺号',max_length=256)
    phone_number = models.CharField('手机号',max_length=32)
    last_uuid = models.CharField('最近一单识别码',max_length=256)
    last_time = models.DateTimeField('最近做单时间',default = time.time())