# Generated by Django 4.0.1 on 2022-01-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0011_alter_post_postphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postPhoto',
            field=models.ImageField(default='images/photo_2021-12-02_23-17-12_F9xv3po.jpg', upload_to='images/'),
        ),
    ]
