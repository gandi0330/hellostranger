# Generated by Django 3.2.8 on 2021-10-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_auto_20211007_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='play1_title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='play2_title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='play3_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
