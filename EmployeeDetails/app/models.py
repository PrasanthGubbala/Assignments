from django.db import models

class Employeedetails(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    location = models.IntegerField()
    salary = models.FloatField()
