# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_management', '0003_scorecard_passed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_id']},
        ),
        migrations.AlterField(
            model_name='instructor',
            name='course_offered',
            field=models.ManyToManyField(blank=True, null=True, to='class_management.Course'),
        ),
    ]