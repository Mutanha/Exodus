# models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # ...

class Company(models.Model):
    name = models.CharField(max_length=100)
    company_id = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    # ...

