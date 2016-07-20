# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0017_auto_20160711_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='zone_commodity',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_altPhone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_exp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
