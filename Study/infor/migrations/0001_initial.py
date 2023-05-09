# Generated by Django 4.0.5 on 2023-05-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True, verbose_name='用户昵称')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
                ('truename', models.CharField(max_length=16, verbose_name='真实姓名')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='用户邮箱')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='电话号码')),
            ],
        ),
    ]