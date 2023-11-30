from django.db import models
from django.contrib.auth.models import User

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
    route = models.CharField(max_length=50, default='treasury')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1) #USER ID
    #NUEVOS CAMPOS
    monto = models.IntegerField(default=0)
    id_admin_turn = models.IntegerField(default=0)# EL ID DEL ADMINISTRADOR QUE POSEA ESTE FUT (no lo hice con FK por que el fut no pertenece a ningun admin)
    pay_type = models.CharField(max_length=50, default='deposito')# tipo de pago ('deposito' o 'pasarela')
    img_pay = models.BinaryField(default=b'')
    report_state = models.BooleanField(default=False)
    finisher_state = models.BooleanField(default=False)# ESTE BOOLEAN DETERMINA SI EL TRAMITE ACABO (el director al emitir tramite modificara este boolean)

    def __str__(self):
        return f"ID: {self.id} - {self.name} - {self.order} - {self.email}"

class tupa(models.Model):
    areas_incolucradas = models.CharField(max_length=100)
    tipo_de_servicio = models.CharField(max_length=100)
    monto = models.IntegerField()
    duracion_de_tramite = models.IntegerField()
    procedimiento = models.CharField(max_length=200)
    require_attach = models.BooleanField(default=False)

    def __str__(self):
        return f"ID: {self.id} - {self.tipo_de_servicio} - {self.monto} - {self.duracion_de_tramite}"

