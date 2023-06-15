from django.db import models
from myapp.models import fut

import random
import string

# Create your models here.

# funcion para generar un coddigo de 7 caracteres incluyendo 'letras mayusculas y minusculas y numeros'
def generate_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(7))
    return code

class Admins(models.Model):
    AREA_OPTIONS = [
        ('treasury', 'Tesoreria'),
        ('secretary', 'Secretaria'),
        ('direction', 'Direccion'),
    ]
    name = models.CharField(max_length=25)
    fullname = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    position = models.CharField(max_length=25, choices=AREA_OPTIONS)
    phone = models.CharField(max_length=12)
    dni = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    code = models.CharField(max_length=7, unique=True, default=generate_code)

    # endcoede generate
    def __str__(self):
        return self.name+" "+self.fullname+" - "+self.position+" - "+self.email+" - "+self.phone+" - "+self.dni+" - "+self.password

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
    

class certificate(models.Model):
    tittle = models.CharField(max_length=40)
    pdf_binary = models.BinaryField(default=b'')
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE, default=3)
    state = models.BooleanField()
    def __str__(self):
        return self.tittle+" - "+self.fut_id