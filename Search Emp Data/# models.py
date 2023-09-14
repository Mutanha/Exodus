# models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year_started = models.IntegerField()
    year_left = models.IntegerField(null=True, blank=True)
    # ... other fields
