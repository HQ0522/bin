# Generated by Django 4.0.5 on 2023-05-04 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infor', '0002_course_rename_truename_user_realname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_time',
        ),
    ]
