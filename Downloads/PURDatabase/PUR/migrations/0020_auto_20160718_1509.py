# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0019_auto_20160718_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='acreage',
        ),
        migrations.AddField(
            model_name='zone',
            name='acreage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
