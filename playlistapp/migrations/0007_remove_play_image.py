# Generated by Django 3.2.8 on 2021-10-12 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlistapp', '0006_play_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play',
            name='image',
        ),
    ]
