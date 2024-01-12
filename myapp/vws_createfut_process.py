from asgiref.sync import sync_to_async, async_to_sync
from django.shortcuts import render
from .models import fut, tupa
from myapp_admin.models import process
from django.http import HttpResponse, JsonResponse

#pip install qrcode
import random, qrcode


#IMPORTAR VISTAS
from myapp.vws_createfut_process_process import paint_qr_img
from myapp.vws_createfut_process_process import manage_document
#-----------------------------------------------------------------


import base64
import os
from django.conf import settings

def proceedings(request):
    code_ = request.GET.get('code')
    if(code_ == None):
        return HttpResponse("<h1>404 ESTA PAGINA NO EXISTE :(</h1>")
    else:
        object = fut.objects.filter(code=code_).values('id', 'name', 'full_name', 'dni', 'order', 'proceeding', 'password', 'code', 'program', 'email', 'qrimg_binary').first()
        dni = str(object['dni'][:3])
        #Email process
        email = str(object['email'])

        # Extraer en tmp la imagen del qr
        # paint_qr_img(object['id'], object['qrimg_binary']);

        if(email == 'null'):
            email_code = "- - -"
        else:
            print("PUES ES NULL")
            e = email[0]
            l = email[-11]
            nummail = len(email)
            nummail = nummail-12 # (10 de @gmail.com) (2 de los dos digitos que si se ven)

            #generamos los asteriscos
            asterisk = []
            for i in range(nummail):
                asterisk.append('*')
            asterisk_Str = ''.join(asterisk)
            email_code = e+asterisk_Str+l+'gmail.com' #quitamos el @

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
            data = process.objects.filter(stage=i, fut_id_id=object['id']).values('tittle', 'name', 'reception', 'exit', 'num').first()
            loco.append(data)

        left = 20 # css left details picture
        return render(request, 'view_fut/proceedings.html', {
            'fut_id': object['id'],
            'Name': object['name'],
            'Fullname': object['full_name'],
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
            'Data': loco,
            'Num_process': num_registros
        })

# para generear el expediente
async def generate_proceedings():
    # Genramos el número de Expediente
    Expediente = random.sample(range(0, 9),5)
    exp_ = ''.join(map(str, Expediente))
    # Generamos la contraseña
    Contraseña = random.sample(range(0, 9),4)
    pas_ = ''.join(map(str, Contraseña))

    return exp_, pas_


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
    #yag.send(destinatarios, asunto, html)
    return render(request, 'view_fut/functions/my_credentials_EMAIL.html', {'success': True, 'Email':email})

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
    # End
    message = 'successful'
    return JsonResponse({'message': message})


def procedures_list(request):
    tipeo = request.GET.get('tipeo')
    objs = tupa.objects.filter(tipo_de_servicio__startswith=tipeo).order_by('id').values('id', 'tipo_de_servicio')
    result_list = list(objs)
    return JsonResponse({'message': result_list})

def tupa_validation(request):
    id_tupa = request.GET.get("id_tupa")
    objs = tupa.objects.filter(id=id_tupa).values('require_attach', 'tipo_de_servicio', 'procedimiento').first()
    return JsonResponse({'data': objs})

def download_pdf_procedure(request):
    id_fut = request.GET.get('id_fut')
    print(id_fut)

    # OBTENEMOS EL DOCUMENTO Y LO ESCRIBIMOS EN LA CARPETA MEDIA
    tutuloYexpediente = manage_document(id_fut)

    return JsonResponse({'data': tutuloYexpediente})

# ESTA FUNCIÓN FINALMENTE DESCARGA EL ARCHIVO
def direct_download(request):
    if request.method == 'GET':
        fut_id = request.GET.get('id_fut')
        file = 'doc_finisher_tramited_fut_'+str(fut_id)+'.pdf'
        file_path = os.path.join(settings.MEDIA_ROOT, file)
        print(file_path)
        try:
            with open(file_path, 'rb') as f:
                print(file_path)
                response = HttpResponse(f.read(), content_type='application/pdf') #image/jpeg
                response['Content-Disposition'] = 'attachment; filename="%s"' % file
                return response
        except FileNotFoundError:
            print("El archivo no existe.")
            return HttpResponse("<h1>El archivo no existe. :(</h1>")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return HttpResponse("<h1>Ocurrió un error inesperado :(</h1>")
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")