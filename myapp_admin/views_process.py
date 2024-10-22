import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
from myapp_admin.models import process, Admins, document
import os
import io
from django.core.files.base import ContentFile
from io import BytesIO

from myapp_admin.views_get_fut import send_definity, log_verifying

def direction_download(request):
    id = request.GET.get('id')
    
    mi_objeto = document.objects.get(fut_id_id=id)
    binary_field = mi_objeto.pdf_binary
    pdf_binary = base64.b64decode(binary_field)

    ruta_guardar_pdf = 'myapp_admin/static/tmp/test_my_pdf.pdf'
    
    with open(ruta_guardar_pdf, 'wb') as output_pdf:
        output_pdf.write(pdf_binary)

    message = 'sussesfull'
    return JsonResponse({'message': message})

def fut_data(Position):
    objs = fut.objects.exclude(stage__exact=3).filter(route=Position).values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')

    num_no_view = 0 # fut's that not been seen yet
    total_futs = 0 # number of fut's that will shown on the screen
    list_data = [] # data of the fut's

    for i in objs:
        total_futs = total_futs + 1
        if i['view'] == 0:
            num_no_view = num_no_view + 1
    num=1
    for i in objs:
        diccionary={}
        diccionary['id'] = i['id']
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        diccionary['stage'] = i['stage']
        diccionary['view'] = i['view']
        diccionary['num'] = num
        num = num + 1
        list_data.append(diccionary)

    output = {
        "Num_no_view": num_no_view,
        "Total_futs": total_futs,
        "List_data": list_data
    }
    return output

def update_document(fut_id, pdf_binary_encoded):
    up_register = document.objects.get(fut_id_id=fut_id)
    up_register.final_pdf_binary = pdf_binary_encoded
    up_register.save()
    return None

def send_document(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    # (/AQUÍ)(ESTO_SE_REPITE)


    print('Estamoh en send document')
    Position = request.COOKIES.get('log_position')
    data = fut_data(Position)

    # APARTIR DE QUI EMPIEZA EL PROCESO DE 'SEND INSSUED'
    fut_id = request.POST.get('fut_id')
    fut_tittle = request.POST.get('fut_tittle')

    # Ahora Haremos el proceso de 'Send Definitivo'
    #obtenemos la cookie para realizar el proceso de envio
    Position = request.COOKIES.get('log_position')
    message = send_definity('none', fut_id, Position)
    # Fin del 'Send Defintivo'

    print('AQUI OBTENEMOS EL FILE')
    archivo_pdf = request.FILES['my_pdf']
    contenido_bytes = archivo_pdf.read()
        
    pdf_binary_encoded = base64.b64encode(contenido_bytes)

    update_document(fut_id, pdf_binary_encoded)

    return render(request, 'admin/staff_treasury.html', {
        'Object': data["List_data"],
        'views': data["Num_no_view"],
        'total_futs': data["Total_futs"],
        #admin data
        'Data_log': Data_log
    })