# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from class_management.models import Department, Course, Student, Scorecard, Instructor

# Register the models so that they can be accessed in the Django admin center.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Scorecard)
admin.site.register(Instructor)
