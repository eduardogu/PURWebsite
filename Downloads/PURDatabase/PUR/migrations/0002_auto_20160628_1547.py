# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zone',
            old_name='zone_township_dr',
            new_name='zone_township_dir',
        ),
    ]
