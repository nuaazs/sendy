# Generated by Django 4.0.4 on 2022-05-16 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_logs_done_time_alter_logs_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='done_time',
            field=models.DateTimeField(default=1652670700.205887, verbose_name='完成时间或打回时间'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='send_time',
            field=models.DateTimeField(default=1652670700.205878, verbose_name='发单时间'),
        ),
    ]
