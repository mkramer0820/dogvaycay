# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20160720_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='dogs_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_signed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
