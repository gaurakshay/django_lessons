# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import arrow
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    # created_date = models.DateTimeField(default=arrow.now().datetime) # Warns.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_img', blank=True)

    class Meta:
        db_table = 'posts'
        ordering = ['-published_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()
