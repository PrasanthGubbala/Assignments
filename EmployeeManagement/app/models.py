from django.db import models

class EmployeeDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True,primary_key=True)
    password = models.CharField(max_length=30)