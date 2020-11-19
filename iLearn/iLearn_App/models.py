from django.db import models
from datetime import datetime


class TecherRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    designation = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=11)
    def __str__(self):
        return self.name


class ParentRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    relation = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class StudentRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    contact = models.IntegerField()
    parent = models.ForeignKey(ParentRegistration,on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=11)


class ScheduleClass(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=30, unique=True)
    lecture = models.ForeignKey(TecherRegistration,on_delete=models.CASCADE)
    time = models.TimeField()
    status = models.CharField(max_length=30)


class StudentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    class_id = models.IntegerField()
    date = models.DateField()


