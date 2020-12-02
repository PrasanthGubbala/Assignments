from django.db import models


class User(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    contact = models.IntegerField()
    amount = models.FloatField(default=0.0)
    password = models.CharField(max_length=20)


class Card(models.Model):
    card_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




