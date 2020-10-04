from django.db import models
from datetime import datetime

class Organization(models.Model):
    company_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    contact = models.IntegerField()
    def __str__(self):
        return self.company_name


class Departments(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    def __str__(self):
        return self.department

class Designation(models.Model):
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    def __str__(self):
        return self.designation

class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    org  = models.ForeignKey(Organization,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Employees_Attendance_Collection(models.Model):
    employee  = models.ForeignKey(Employees,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now().date())
    status = models.CharField(max_length=8,default='absent')
    start = models.TimeField(default='0:0:0.0')
    end = models.TimeField(default='0:0:0.0')
    break_time = models.TimeField(default='0:0:0.0')
    def __str__(self):
        return self.date