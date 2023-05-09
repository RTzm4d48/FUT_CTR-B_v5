from django.db import models

# Create your models here.

class Admins(models.Model):
    name = models.CharField(max_length=25)
    fullname = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    position = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    dni = models.CharField(max_length=10)
    password = models.CharField(max_length=30)


class process(models.Model):
    tittle = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    reception = models.DateTimeField()
    exit = models.DateTimeField()
    state = models.BooleanField()
    num = models.IntegerField()

