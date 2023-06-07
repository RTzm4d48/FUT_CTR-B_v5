import json
from asgiref.sync import sync_to_async, async_to_sync
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse # agregamos el HttpResponse
from .models import fut
from myapp_admin.models import process, Admins
from datetime import date
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

#pip install qrcode
import random, qrcode

#pip install opencv-python-headless
import cv2
import base64

import string

from django.urls import reverse

# para descargar una imagen
from django.conf import settings
import os

#send email
# py -m pip install yagmail[all]
import yagmail

#para saber el dia y la hora actual
from datetime import datetime

def index(request):
    return render(request,'index.html')

@csrf_exempt
def my_fut(request):
    my_list_ = list(range(10))
    my_list = [i + 5 for i in range(10)]
    var = 5
    return render(request, 'view_fut/fut.html', {
        'some_list': my_list,
        'var': var
    })



def form_new_fut(request):
    return render(request, 'create_fut/identification.html')


def create_fut_process(request):
    if request.method=='POST':
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')

        return render(request, 'create_fut/process.html', {
            'Name': name,
            'Program': program,
            'Dni': dni,
            'Phone': phone,
            'Cycle': cycle,
            'Email': email
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")

    
@csrf_exempt  
def create_fut_pay(request):
    if request.method=='POST':
        # identification
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')
        # Procedimiento con el PDF
        pdf_file = request.FILES['pdf_file']
        pdf_binary = pdf_file.read()
        pdf_binary_encoded = base64.b64encode(pdf_binary)

        return render(request, 'create_fut/pay.html', {
            'Name': name,
            'Program': program,
            'Dni': dni,
            'Phone': phone,
            'Cycle': cycle,
            'Email': email,
            'Myrequest': myrequest,
            'Order': order,
            'Reason': reason,
            'Pdf_binary_encoded': pdf_binary_encoded
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")

# para generear el expediente
async def generate_proceedings():
    # Genramos el número de Expediente
    Expediente = random.sample(range(0, 9),5)
    exp_ = ''.join(map(str, Expediente))
    # Generamos la contraseña
    Contraseña = random.sample(range(0, 9),4)
    pas_ = ''.join(map(str, Contraseña))

    return exp_, pas_


async def generate_code():
    caracteres = string.ascii_letters + string.digits
    code = ''.join(random.choice(caracteres) for i in range(11))
    return code

@sync_to_async
def save_my_objet(name, program, dni, phone, cycle, email, myrequest, order, reason, now_date, pdf_bytes, exp_, pas_, code_, qrimg_bytes):
    my_objet = fut(name=name, program=program, dni=dni, phone=phone, cycle=cycle, email=email, myrequest=myrequest, order=order, reason=reason, date=now_date, pdf_binary=pdf_bytes, proceeding=exp_, password=pas_, code=code_, qrimg_binary=qrimg_bytes)
    my_objet.save()
    new_id = my_objet.id
    return new_id

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

    return img_base64

async def generate_email(email, name, exp_, pas_): 
    email = 'whiteman.play69@gmail.com'
    contraseña = 'hkekvgngsirgtjym'

    yag = yagmail.SMTP(user=email, password=contraseña)

    destinatarios = [email]

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
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><p style="font-size: 16px;margin: auto 2px auto auto;">Expediente: </p><h2 style="margin: auto auto auto 2px;font-size: 16px;">{exp_}</h2></div>
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><P style="font-size: 16px;margin: auto 2px auto auto;">Contraseña</P><h2 style="margin: auto auto auto 2px;font-size: 16px;">{pas_}</h2></div>
            </div>
            <div class="qr" style="width: 150px;height: 150px;margin: 20px auto;">
                <img style="width: 100%;" src="https://i.ibb.co/zRq5c2Z/s-BUWS8kthxqqrcode.png" alt="">
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

@sync_to_async
def save_process(tittle, name, reception, exit, state, num, fut_id, stage):
    my_objet = process(tittle = tittle, name = name, reception = reception, exit = exit, state = state, num = num, fut_id_id = fut_id, stage = stage)
    my_objet.save()

    date_ = datetime.now() 
    date_format = date_.strftime("%Y-%m-%d %H:%M:%S")

    up_process = process.objects.get(stage=0, fut_id_id=fut_id)
    up_process.exit = date_format
    
@sync_to_async
def name_admin(position):
    objs = Admins.objects.filter(position=position).values('name', 'fullname').first()
    name = objs['name']+' '+objs['fullname']
    return name


async def finisher(request):
    if request.method == 'POST':
         # identification
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')
        pdf_memoryview = request.POST.get('pdf_binary_encoded')
        pdf_bytes = pdf_memoryview.encode("utf-8")

        now_date = date.today()
        
        exp_, pas_ = await generate_proceedings()
        code_ = await generate_code()
        qrimg_bytes = await generate_qrcode(code_)

        nnn = await generate_email(email, name, exp_, pas_)

        new_id = await save_my_objet(name, program, dni, phone, cycle, email, myrequest, order, reason, now_date, pdf_bytes, exp_, pas_, code_, qrimg_bytes)

        # CRUD en el modelo 'Process'
        #obtener the date
        date_ = datetime.now() 
        date_format = date_.strftime("%Y-%m-%d %H:%M:%S")

        await save_process('TRAMITE EN CURSO', 'INSTITUTO LATINOAMERICANO SIGLO XXI', date_format, date_format, False, 20, new_id, 0)
        # obtenemos el nombrede la tesoreria para introducirlo en el modelo process
        admin_name = await name_admin('treasury')
        await save_process('TESORERIA', admin_name, date_format, None, False, 40, new_id, 1)

        response = redirect('n_successful')
        response.set_cookie('New_id', new_id)
        return response
    
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    
    
def successful(request):
    my_id = request.COOKIES.get('New_id')
    objetos = fut.objects.filter(id=my_id).values('name', 'dni', 'order', 'proceeding', 'password', 'code').first()
    return render(request, 'create_fut/successful.html', {
        'Name': objetos['name'],
        'Dni': objetos['dni'],
        'Order': objetos['order'],
        'Code': objetos['code'],
        'Proceeding': objetos['proceeding'],
        'Password': objetos['password']
    })

def proceedings(request):
    code_ = request.GET.get('code')
    object = fut.objects.filter(code=code_).values('id', 'name', 'dni', 'order', 'proceeding', 'password', 'code', 'program', 'email').first()
    dni = str(object['dni'][:3])
    #Email process
    email = str(object['email'])
    e = email[0]
    l = email[-11]
    nummail = len(email)
    nummail = nummail-12 # (10 de @gmail.com) (2 de los dos digitos que si se ven)

    #generamos los asteriscos
    asterisk = []
    for i in range(nummail):
        asterisk.append('*')
    asterisk_Str = ''.join(asterisk)
    email_code = e+asterisk_Str+l+'@gmail.com'

    # My params for css
    progressbar = list(range(9)) # for progress bar lines

    details = []
  
    x = 20
    for i in range(4):# aquí ponemos el numero de cuadros de detalles que habra en la interfaz
        details.append(x)
        x += 20
    # LO QUE VENDRA DE UNA BASE DE DATOS:
    my_id = 1
    loco = []
    
    num_registros = process.objects.filter(fut_id_id=object['id']).count()
    print("Hay {} registros con MiModelo_id igual a 3".format(num_registros))

    for i in range(num_registros):
        data = process.objects.filter(stage=i).values('tittle', 'name', 'reception', 'exit', 'num').first()
        loco.append(data)
    

    left = 20 # css left details picture
    return render(request, 'view_fut/proceedings.html', {
        'Name': object['name'],
        'Dni': dni,
        'Order': object['order'],
        'Proceeding': object['proceeding'],
        'Program': object['program'],
        'Progressbar': progressbar,
        'Details': details,
        'Left': left,
        'Email_code': email_code,
        'Email': email,
        'Password': object['password'],
        'Data': loco
    })


def send_email(request):
    send_email = request.GET.get('gmail')
    name = request.GET.get('name')
    proceeding = request.GET.get('proceeding')
    password = request.GET.get('password')
    # Proceso de envio de correo
    email = 'whiteman.play69@gmail.com'
    contraseña = 'hkekvgngsirgtjym'

    yag = yagmail.SMTP(user=email, password=contraseña)

    destinatarios = [send_email]

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
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><p style="font-size: 16px;margin: auto 2px auto auto;">Expediente: </p><h2 style="margin: auto auto auto 2px;font-size: 16px;">{proceeding}</h2></div>
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><P style="font-size: 16px;margin: auto 2px auto auto;">Contraseña</P><h2 style="margin: auto auto auto 2px;font-size: 16px;">{password}</h2></div>
            </div>
            <div class="qr" style="width: 150px;height: 150px;margin: 20px auto;">
                <img style="width: 100%;" src="https://i.ibb.co/zRq5c2Z/s-BUWS8kthxqqrcode.png" alt="">
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
    # End
    message = 'successful'
    return JsonResponse({'message': message})


def download_image(request):
    image_name = 'doc.pdf'
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    
    print('-----RUTA DEL PATH-----'+image_path)
    
    with open(image_path, 'rb') as f:
         response = HttpResponse(f.read(), content_type='image/jpeg')
         response['Content-Disposition'] = 'attachment; filename="%s"' % image_name
         return response
    #return render(request, 'view_fut/download_image.html')

def my_credentials_email(request):
    send_email = 'tapieese500@gmail.com'
    name = 'Edgar Sanchez'
    proceeding = '98765'
    password = '9878'

    email = 'whiteman.play69@gmail.com'
    contraseña = 'hkekvgngsirgtjym'

    #yag = yagmail.SMTP(user=email, password=contraseña)

    destinatarios = [send_email]

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
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><p style="font-size: 16px;margin: auto 2px auto auto;">Expediente: </p><h2 style="margin: auto auto auto 2px;font-size: 16px;">{proceeding}</h2></div>
                <div class="proce" style="background: white;display: flex;width: 80%;margin: 8px auto;height: 50px;"><P style="font-size: 16px;margin: auto 2px auto auto;">Contraseña</P><h2 style="margin: auto auto auto 2px;font-size: 16px;">{password}</h2></div>
            </div>
            <div class="qr" style="width: 150px;height: 150px;margin: 20px auto;">
                <img style="width: 100%;" src="https://i.ibb.co/zRq5c2Z/s-BUWS8kthxqqrcode.png" alt="">
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
    #yag.send(destinatarios, asunto, html)


    return render(request, 'view_fut/functions/my_credentials_EMAIL.html', {'success': True, 'Email':email})
