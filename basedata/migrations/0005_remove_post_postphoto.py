# Generated by Django 4.0.1 on 2022-01-11 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0004_post_postphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postPhoto',
        ),
    ]