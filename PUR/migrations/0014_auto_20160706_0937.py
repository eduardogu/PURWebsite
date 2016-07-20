# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUR', '0013_auto_20160703_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_name', models.CharField(max_length=40)),
                ('commodity_code', models.CharField(max_length=5)),
                ('qualifier', models.CharField(blank=True, max_length=2, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='product_measurement',
            field=models.CharField(default='oz', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='block_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]