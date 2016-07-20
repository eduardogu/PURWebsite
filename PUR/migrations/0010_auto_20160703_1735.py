# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0009_auto_20160703_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticide',
            name='dateEntered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pesticide',
            name='manuAddress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pesticide',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
