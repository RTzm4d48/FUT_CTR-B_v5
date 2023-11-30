# VISTA generate_proceedings
import random, qrcode

# VISTA generate_code
import string

# VISTA generate_qrcode
#pip install opencv-python-headless
import cv2
import base64

# VISTA generate_email
# py -m pip install yagmail[all]
import yagmail

# VISTA save_my_objet
from .models import fut, tupa
from myapp_admin.models import ruta_tramite, Admins, notification
from asgiref.sync import sync_to_async, async_to_sync

# VISTA guardar_archivo_enTmp
from django.core.files.storage import FileSystemStorage

# PARA GENERAR EL PASS Y EL NUM DE EXPEDINETE
async def generate_proceedings():
    # Genramos el número de Expediente
    Expediente = random.sample(range(0, 9),5)
    exp_ = ''.join(map(str, Expediente))
    # Generamos la contraseña
    Contraseña = random.sample(range(0, 9),4)
    pas_ = ''.join(map(str, Contraseña))

    return exp_, pas_

# PARA GENERAR EL NOMBRE DEL ARCHIVO img QR
async def generate_code():
    caracteres = string.ascii_letters + string.digits
    code = ''.join(random.choice(caracteres) for i in range(11))
    return code

# PARA GENERAR LA IMAGEN QR
async def generate_qrcode(code_):
    print('Hay que crear el QR!')

    input = 'http://127.0.0.1:8000/my_fut/proceedings?code='+code_

    qr = qrcode.QRCode(version=1, box_size=10, border=3)
    qr.add_data(input)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    static_path = 'myapp/static/tmp/'+code_+'qrcode.png'

    print(static_path)
    img.save(static_path)
    img = cv2.imread(static_path)
    
    # Codificar la imagen en formato PNG
    retval, buffer = cv2.imencode('.png', img)

    # Convertir el buffer a bytes
    img_bytes = buffer.tobytes()

    # Codificar los bytes en base64
    img_base64 = base64.b64encode(img_bytes)

    # print(img_base64)
    print('Se genero la img del qr exitosamente!')

    return img_base64

# ESTA FUNCIÓN SE ENCARGA DE ENVIAR GMAILS
async def generate_email(email, name, exp_, pas_):
    autor_email = 'whiteman.play69@gmail.com'
    contraseña = 'hkekvgngsirgtjym'

    yag = yagmail.SMTP(user=autor_email, password=contraseña)

    destinatarios = "tapieese500@gmail.com" #email
    asunto = 'Credenciales ILS'
    html = f'''
    <div class="contentsend_father" style="width: 100%;color:black;">
        <div class="contentsend" style="background: #F0F1F5;width: 90%;display: block;padding: 20px;margin: auto;">
        <div class="contentlogo" style="text-align: center;">
            <img width="40%" src="https://i.ibb.co/W0p4JZ2/logoils-01-01.png" alt="">
        </div>
        <div class="info" style="text-align: center;font-family: Arial, Helvetica, sans-serif;">
            <h2>Hola {name}!</h2>
            <p style="text-align: left;font-size: 15px;">Estas son las credenciales del trámite que se hizo vinculado a esta cuenta de gmail.</p>
        </div>
        <div class="contentcredentials" style="width: 80%;margin: auto;padding: 1px;">
            <div class="contentlog" style="padding: 1px;font-family: Arial, Helvetica, sans-serif;">
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;">
                    <p style="font-size: 16px;margin: auto 2px auto auto;">Expediente: </p><h2 style="margin: auto auto auto 2px;font-size: 16px;">{exp_}</h2>
                </div>
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;">
                    <P style="font-size: 16px;margin: auto 2px auto auto;">Contraseña</P><h2 style="margin: auto auto auto 2px;font-size: 16px;">{pas_}</h2>
                </div>
            </div>
            <div class="qr" style="width: 150px;height: 150px;margin: 20px auto;">
                <img style="width: 100%;" src="https://i.ibb.co/V0GrnzK/79-XNZx-F1cu-Aqrcode.png" alt="">
            </div>
        </div>
        <div class="info" style="text-align: center;font-family: Arial, Helvetica, sans-serif;">
            <p style="text-align: left;font-size: 15px;">Este gmail se ha generado debido a que se usó al realizar un trámite en la página del instituto ILS</p>
            <p style="text-align: left;font-size: 15px;">Si no estás intentando realizar un trámite en ILS ignora este correo.</p>
        </div>
        </div>
        <div style="width: 80%;margin: 20px auto 0px auto;" class="infopadd">
        <p style="margin: 0px;font-family: Arial, Helvetica, sans-serif;font-size: small;margin: 10px auto;">Este correo se envió a la dirección de correo electrónico asociado a un trámite en ILS</p>
        <p style="margin: 0px;font-family: Arial, Helvetica, sans-serif;font-size: small;margin: 10px auto;">Este correo electrónico se genera automáticamente. Por favor no responder a él. Si necesita ayuda adicional. Por favor contacte con nuestro equipo de soporte.</p>
        <a href="#">www.ils.com/help</a>
        </div>
    </div>
    '''
    yag.send(destinatarios, asunto, html)
    return name

# ESTO ES PARA GUARDAR FUT EN LA DB
@sync_to_async
def save_my_objet(name, program, dni, phone, cycle, email, myrequest, order, reason, now_date, attach_byte, exp_, pas_, code_, qrimg_bytes, monto, id_admin_turn, img_pay, pay_type, id_user):
    my_objet = fut(name=name, program=program, dni=dni, phone=phone, cycle=cycle, email=email, myrequest=myrequest, order=order, reason=reason, date=now_date, pdf_binary=attach_byte, proceeding=exp_, password=pas_, code=code_, user_id_id=id_user, qrimg_binary=qrimg_bytes, monto=monto, id_admin_turn=id_admin_turn, img_pay=img_pay, pay_type=pay_type)
    my_objet.save()
    new_id = my_objet.id
    return new_id

# OBTENERMOS EL MONTO DEL MODELO tupa
@sync_to_async
def get_monto(order_id):
    obj = tupa.objects.filter(id=order_id).values('monto').first()
    monto = obj['monto']
    return monto

# GUARDAR EN LA CARPETA tmp ARCHIVOS
def guardar_archivo_enTmp(pdf_file):
    #GUARDAREMOS EL PDF
    print("ESTAMOH GUARDANDO LO")
    static_path = 'myapp/static/tmp/'
    fs = FileSystemStorage(location=static_path)
    fs.save(pdf_file.name, pdf_file)
    return 'true'

# OBTENEMOS LO QUE SE GUARDO EN LA CARPETA tmp y LO DEBOLVEMOS EN bytes
async def obtener_archivo_deTmp(attach_file_name):
    if(attach_file_name != "false"):
        print("LEEMOS EL ARCHIVO "+attach_file_name+" DE tmp")
        static_path = 'myapp/static/tmp/'+attach_file_name
        # Lee el contenido del archivo en modo binario
        with open(static_path, 'rb') as file:
            file_bytes = file.read()
            file_binary_encoded = base64.b64encode(file_bytes)
        return file_binary_encoded
    else:
        print("BACIO")
        return b''# bynary bacio

# GUARDAMOS EL PRIMER PROCESS
@sync_to_async
def save_process(tittle, name, reception, exit, fut_id):
    my_objet = ruta_tramite(tittle = tittle, name = name, reception = reception, exit = exit, fut_id_id = fut_id)
    my_objet.save()
    # up_process = process.objects.get(stage=0, fut_id_id=fut_id)
    # up_process.exit = exit
    return "successfull"

# OBTENEMOS EL NOMBRE DEL PERSONAL ADMIN
@sync_to_async
def name_admin(position):
    objs = Admins.objects.filter(position=position).values('name', 'fullname').first()
    name = objs['name']+' '+objs['fullname']
    return name

# INCERTAR NOTIFICAIÓN
@sync_to_async
def insert_notification(new_id, id_user, date_format):
    my_objet = notification(tittle = "Creado", date = date_format, emitido = "alumno", tipo = "FUT Creado", fut_id_id=new_id, user_id_id=id_user)
    my_objet.save()
    return 'successfull'