# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 13:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180515_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 13, 50, 38, 757488, tzinfo=utc)),
        ),
    ]
