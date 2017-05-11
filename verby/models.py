# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Writer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pen_Name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=350)
    password = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    gender_choices = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            )
    gender = models.CharField(
            max_length=15,
            choices=gender_choices,
            )


class Publication(models.Model):
    title = models.CharField(max_length=300)
    pen_name = models.ForeignKey(Writer)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=50000)
