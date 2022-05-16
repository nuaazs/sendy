# Generated by Django 4.0.4 on 2022-05-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('short_name', models.CharField(max_length=16)),
                ('limit', models.IntegerField()),
                ('remain', models.IntegerField()),
                ('changed_time', models.DateTimeField(default=1652633028.041645, verbose_name='保存日期')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('isroot', models.IntegerField()),
                ('gender', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]