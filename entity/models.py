from django.db import models

class User(models.Model):
    username = models.CharField(max_length=225,unique=True)
    password = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
    def __str__(self):
        return self.username
class Human(models.Model):
    humanName = models.CharField(max_length=225)
    def __str__(self):
        return self.humanName
class Finance(models.Model):
    humanName = models.ForeignKey(Human,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=225)
    price = models.IntegerField()
    des = models.TextField()
    status = models.CharField(max_length=225)
    createAt = models.DateField(auto_now_add=True)
    endAt = models.DateField(null=True)
    deadline =models.DateField(null=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
