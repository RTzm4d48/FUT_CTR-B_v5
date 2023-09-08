import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
from myapp_admin.models import process, Admins, certificate
import os
import io
from django.core.files.base import ContentFile
from io import BytesIO

def direction_download(request):
    id = request.GET.get('id')
    print("Estamos en direcction download y la direccion de id es: "+id)
    #mi_objeto = certificate.objects.filter(fut_id_id = 20).values('pdf_binary').first()
    mi_objeto = certificate.objects.get(fut_id_id=id)
    
    binary_field = mi_objeto.pdf_binary

    image_binary = base64.b64decode(binary_field)

    ruta_guardar_pdf = 'myapp_admin/static/tmp/el_pedeefe_v1.pdf'


    with open(ruta_guardar_pdf, 'wb') as output_image:
        output_image.write(image_binary)
    
    message = 'sussesfull'
    return JsonResponse({'message': message})