# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_management', '0002_auto_20180515_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecard',
            name='passed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
