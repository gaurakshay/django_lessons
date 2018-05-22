# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse

from nucleus.settings import MEDIA_URL


class Department(models.Model):
    """
    Model that stores the department details.
    Primary key is the department key.
    """
    class Meta:
        db_table="departments"
    department_name = models.CharField(max_length=200)
    department_code = models.CharField(max_length=5, primary_key=True)
    department_chair = models.CharField(max_length=200)

    def __unicode__(self):
        """
        String representation of the object.
        :return: Department name in unicode.
        """
        return self.department_name


class Course(models.Model):
    """
    Model to store the course details.
    The primary key is a compound key (combination of department code and course number).
    """
    class Meta:
        """
        Defines the compound primary key for this object.
        Also defines the table name for the object.
        """
        unique_together = (('course_dept_code', 'course_num_code'), )
        db_table = 'courses'
    course_dept_code = models.ForeignKey(Department)
    course_num_code = models.IntegerField()
    course_name = models.CharField(max_length=200)
    course_seats = models.IntegerField()
    course_description = models.TextField(blank=True)

    def __unicode__(self):
        return self.course_name


class Student(models.Model):
    """
    Model to store the student details.
    The primary key is the student id.
    """
    class Meta:
        """
        Defines the table name for this object.
        Also defines the default ordering for this object list.
        """
        db_table = 'students'
        ordering = ['student_id']
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    stud_pic = models.ImageField(upload_to='student_pics', blank=True)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        """
        String representation of the object.
        :return: Return the string form of the object.
        """
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        """
        Returns the URL for this object (to show student details).
        :return: URL that shows the details for instructor object.
        """
        return reverse('student_details', kwargs={'pk': self.pk})

    def pic_or_default(self):
        """
        Method that returns an appropriate image for the student.
        If the image is available, returns that image, otherwise,
        returns the default image.
        :return: Image to display for the student.
        """
        if self.stud_pic:
            return self.stud_pic.url
        return MEDIA_URL+'student_pics/default.png'

    def course_list(self):
        """
        Get the list of courses that every student takes.
        :return: List of courses in csv format.
        """
        course_list = list()
        for course in self.courses.all():
            course_list.append(course.course_name)
        return ', '.join(course_list)


class Scorecard(models.Model):
    """
    Model to store the student's scores in the courses that the student has taken.
    """
    class Meta:
        """
        Define the table name for storing this model in db.
        """
        db_table = 'scorecard'
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    passed = models.BooleanField()


class Instructor(models.Model):
    """
    Model to store which instructor offers what course.
    """
    class Meta:
        """
        Define the table name for storing this model in db.
        """
        db_table = 'instructors'
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    course_offered = models.ManyToManyField(Course, blank=True)

    def __unicode__(self):
        """
        String representation of the object.
        :return: Unicode representation of the object.
        """
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        """
        Return the url to display this models details.
        :return: Link to display the details for this instructor's pk.
        """
        return reverse('instructor_edit', kwargs={'pk': self.pk})

    def course_list(self):
        """
        List of courses that this instructor offers.
        :return: List in csv format of the courses offered by this instructor.
        """
        course_list = list()
        for course in self.course_offered.all():
            course_list.append(course.course_name)
        return ", ".join(course_list)
