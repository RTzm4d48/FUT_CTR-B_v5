from django.db import models
from myapp.models import fut
from django.contrib.auth.models import User

import random
import string

# Create your models here.

# funcion para generar un coddigo de 7 caracteres incluyendo 'letras mayusculas y minusculas y numeros'
def generate_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(7))
    return code

def generate_code_2():
    letras_permitidas = 'abcdfghijkmnopqrstuvwyz12345667890ABCDFGHIJKMNOPQRSTUVWYZ'  # 'abcdefghijk'
    return ''.join(random.choice(letras_permitidas) for _ in range(6))

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
    route = models.CharField(max_length=40, default='noname')
    def __str__(self):
        num_id = str(self.fut_id.id)
        return self.tittle+" - "+self.name+" - "+num_id
    

class document(models.Model):
    tittle = models.CharField(max_length=40)
    pdf_binary = models.BinaryField(default=b'')
    final_pdf_binary = models.BinaryField(default=b'')
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE, default=3)
    state = models.BooleanField()
    def __str__(self):
        num_id = str(self.fut_id.id)
        return self.tittle+" - "+num_id

#FUT Y FUNCIONES
class reportes(models.Model):
    menssage = models.CharField(max_length=200)
    description = models.TextField()
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE, db_constraint=False)# EL db_constraint=False ES PARA COLOCAR CUALQUIER NÚMERO EN EL id Y NO VALIDARLO
    id_destino_admin = models.IntegerField() #Id admin al que se le evviara el reporte
    id_origen_admin = models.ForeignKey(Admins, on_delete=models.CASCADE, db_constraint=False) #id admin del que envia el reporte
    date = models.DateField(null=True)

    def __str__(self):
        the_fut = str(self.fut_id.id)
        return f"ID: {self.id} - {self.menssage} - {the_fut}"

# MODELOS PARA LA CREACION Y GESTION DE TICKETS
class ticket(models.Model):
    name_creator = models.CharField(max_length=60)
    charge = models.CharField(max_length=60) #CARGO ejem. (tesorera), (alumno)
    tittle = models.CharField(max_length=150)
    state = models.BooleanField(default=False) #NOS SIRVE PARA EL TEMA DE ACTIVACIÓN DEL TICKET
    num_ticket = models.IntegerField()
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admins, on_delete=models.CASCADE) #ADMIN ID
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #USER ID
    view = models.BooleanField(default=False)
    # NEW DATES
    code = models.CharField(max_length=6, default=generate_code_2)
    def __str__(self):
        the_fut_id = str(self.fut_id.id)
        the_admin_id = str(self.admin_id.id)
        the_user_id = str(self.user_id.id)
        return f"ID: {self.id} - {self.name_creator} - {self.num_ticket} - {the_fut_id} - {self.state}"

class ticket_desarrollo(models.Model):
    name = models.CharField(max_length=60)
    desarrollo = models.TextField()
    charge = models.CharField(max_length=60) #CARGO ejem. (tesorera), (alumno)
    date = models.DateTimeField(null=True)
    ticket_id = models.ForeignKey(ticket, on_delete=models.CASCADE)
    img_identify = models.BinaryField(default=b'')# imagen sello de identificacion solo para admins
    def __str__(self):
        the_ticket_id = str(self.ticket_id.id)
        return f"ID: {self.id} - {self.name} - {self.charge} - {the_ticket_id}"

class ticket_attach_file(models.Model):
    name = models.CharField(max_length=60)
    the_type = models.CharField(max_length=10)
    the_size = models.IntegerField()
    the_file = models.BinaryField(default=b'')
    desarrollo_id = models.ForeignKey(ticket_desarrollo, on_delete=models.CASCADE)
    def __str__(self):
        the_desarrollo_id = str(self.desarrollo_id.id)
        return f"ID: {self.id} - {self.name} - {self.the_type} - {the_desarrollo_id}"

class ticket_url(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=200)
    desarrollo_id = models.ForeignKey(ticket_desarrollo, on_delete=models.CASCADE)
    def __str__(self):
        the_desarrollo_id = str(self.desarrollo_id.id)
        return f"ID: {self.id} - {self.name} - {the_desarrollo_id}"

class notification(models.Model):
    tittle = models.CharField(max_length=150)# IRA EL TITULO DE LOS REPORTE O ACLARACIONES DE PROCESADOS
    date = models.DateTimeField(null=True)
    emitido = models.CharField(max_length=60)# AQUI IRA EL NOMBRE DEL ADMINISTRADOR QUE GENERO ESTA NOTIficación
    tipo = models.CharField(max_length=150)# AQUI ACLARAREMOS EL TIPO DE LA NOTI ('procesado', 'reportado a tesoreria', 'reportado a direción', 'finalizacion de tramite')
    view = models.BooleanField(default=False)
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #USER ID

    def __str__(self):
        return f"ID: {self.id} - {self.tittle}"

class ticket_notififcation(models.Model):
    tittle = models.CharField(max_length=150)# IRA EL TITULO DE LOS REPORTE O ACLARACIONES DE PROCESADOS
    desarrollo = models.TextField()
    date = models.DateTimeField(null=True)
    emitido = models.CharField(max_length=60)# AQUI IRA EL NOMBRE DEL ADMINISTRADOR QUE GENERO ESTA NOTIficación
    charge = models.CharField(max_length=60) #CARGO ejem. (tesorera), (alumno)
    view = models.BooleanField(default=False)
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #USER ID

    def __str__(self):
        return f"ID: {self.id} - {self.tittle}"

class ruta_tramite(models.Model):
    tittle = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    reception = models.DateTimeField()
    exit = models.DateTimeField(null=True)
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    
    def __str__(self):
        num_id = str(self.fut_id.id)
        return self.tittle+" - "+self.name+" - "+num_id

# ESTE MODELO ES PARA CUANDO SECRETARIA PROCESE LE DOCUMENTO ENVIANDOSELO A DIRECCIÓN
class secretary_send_document(models.Model):
    tittle = models.CharField(max_length=300)# Aqui iral el order, lo que se esta solicitando en el fut
    the_file = models.BinaryField(default=b'')# PDF
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    coment = models.TextField()

    def __str__(self):
        id_fut = str(self.fut_id.id)
        return id_fut+" - "+self.tittle

# ESTE MODELO ES PARA CUANDO DIRECCION PUBLIQUE EL DOCUMENTO
class direction_public_document(models.Model):
    tittle = models.CharField(max_length=300)# Aqui iral el order, lo que se esta solicitando en el fut
    the_file = models.BinaryField(default=b'')# PDF
    fut_id = models.ForeignKey(fut, on_delete=models.CASCADE)
    expediente = models.CharField(max_length=50)

    def __str__(self):
        id_fut = str(self.fut_id.id)
        return id_fut+" - "+self.tittle
