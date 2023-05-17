from django.db import models
from myapp.models import fut

# Create your models here.

class Admins(models.Model):
    name = models.CharField(max_length=25)
    fullname = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    position = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    dni = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name+" "+self.fullname+" - "+self.position

class process(models.Model):
    tittle = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    reception = models.DateTimeField()
    exit = models.DateTimeField(null=True)
    state = models.BooleanField()
    num = models.IntegerField()
    stage = models.IntegerField(default=0)
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE, default=3)
    def __str__(self):
        return self.tittle+" - "+self.name