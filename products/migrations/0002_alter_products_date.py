# Generated by Django 4.0.4 on 2022-05-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(default=1652668276.357514, verbose_name='计划发单日期'),
        ),
    ]