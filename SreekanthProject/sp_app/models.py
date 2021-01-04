from django.db import models


# class User(models.Model):
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     username = models.CharField(max_length=30,unique=True)
#     email = models.EmailField(unique=True)
#     contact = models.IntegerField(primary_key=True)
#     address = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     password = models.CharField(max_length=10)
#     def __str__(self):
#         return self.username

class Projects(models.Model):
    title =  models.CharField(max_length=30)
    technology = models.CharField(max_length=30)
    describe = models.CharField(max_length=1000)
    duration = models.IntegerField()
    affordable_amount = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    status = models.CharField(max_length=15,default='on-going')
    def __str__(self):
        return self.title
