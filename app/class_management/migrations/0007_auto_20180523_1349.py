# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_management', '0006_auto_20180522_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.IntegerField(max_length=3)),
                ('number', models.IntegerField(max_length=7)),
            ],
            options={
                'db_table': 'phone_numbers',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='phones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='class_management.PhoneNumber'),
        ),
    ]
