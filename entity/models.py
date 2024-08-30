from django.db import models

class User(models.Model):
    username = models.CharField(max_length=225,unique=True)
    password = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
class Finance(models.Model):
    humanName = models.CharField(max_length=225)
    type = models.CharField(max_length=225)
    price = models.IntegerField()
    des = models.TextField()
    status = models.CharField(max_length=225)
    createAt = models.DateField(auto_now_add=True)
    endAt = models.DateField()
    deadline =models.DateField()
class Human(models.Model):
    humanName = models.CharField(max_length=225)