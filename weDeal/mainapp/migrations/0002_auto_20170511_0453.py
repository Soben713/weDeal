# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='sold_items',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deal',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
