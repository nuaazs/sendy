# Generated by Django 4.0.4 on 2022-05-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer', models.CharField(max_length=256, verbose_name='刷手旺旺号')),
                ('send_time', models.DateTimeField(default=1652664979.5038688, verbose_name='发单时间')),
                ('done_time', models.DateTimeField(default=1652664979.5038779, verbose_name='完成时间或打回时间')),
                ('sender', models.CharField(max_length=256, verbose_name='发单人')),
                ('pic_url', models.CharField(max_length=256, verbose_name='主图链接')),
                ('uuid', models.CharField(max_length=256, verbose_name='识别码')),
                ('isback', models.IntegerField(verbose_name='是否打回')),
                ('isdone', models.IntegerField(verbose_name='是否完成')),
            ],
        ),
    ]