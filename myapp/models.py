from django.db import models

# Create your models here.

class fut(models.Model):
    # Solicitante
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    dni = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    cycle = models.CharField(max_length=2)
    email = models.TextField(default='')
    # Registro
    myrequest = models.TextField()
    order = models.CharField(max_length=300)
    reason = models.TextField()
    date = models.DateField()
    pdf_binary = models.BinaryField(default=b'')
    proceeding = models.TextField() # Expediente
    password = models.TextField()
    #imagen QR
    qrimg_binary = models.BinaryField(default=b'')
    code = models.TextField(default='00000000000')
    stage = models.IntegerField(default=0)
    #view es pa que en la interfas figure si el registro fue abrierto o no
    view = models.BooleanField(default=False)
    n_ticket = models.CharField(max_length=30, default='0000000000')

    #la ruta en la que se encuentra(tersoreria, secretaria...)
    route = models.CharField(max_length=50, default='treasurer')

    def __str__(self):
        return self.name+" - "+self.order+" - "+self.email