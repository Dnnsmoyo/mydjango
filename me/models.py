# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title
