# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0011_auto_20160703_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticide',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
