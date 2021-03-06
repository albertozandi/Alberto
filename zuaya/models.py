# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Cuisine(models.Model):
    """
    This class defines the database model for the cuisine.
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.IntegerField()
