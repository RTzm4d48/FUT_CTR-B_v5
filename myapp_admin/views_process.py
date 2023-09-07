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
    
    #binary_data = mi_objeto['pdf_binary']
    binary_field = mi_objeto.pdf_binary
    
    ruta_guardar_pdf = 'myapp_admin/static/tmp/nuevo_archivo.pdf'
    

    binary_data = binary_field.read()
    # ESCRIBIR EL ARCHIVO BINARIO EN UN ARCHIVO PDF
    # WRITE THE BINARY FILE TO A PDF FILE

    #pdf_file = BytesIO(binary_data)

    # Crea un objeto BytesIO y escribe los datos binarios en él
    pdf_file = io.BytesIO(binary_data)

    # Crea un archivo PDF a partir de los datos binarios
    pdf_content = ContentFile(pdf_file.read(), 'miarchivo.pdf')
    print("COMPRUEVO")
    pdf_content.save(ruta_guardar_pdf)

    #with open(ruta_guardar_pdf, 'wb') as output_pdf:
    #    output_pdf.write(pdf_file.getbuffer())

    message = 'sussesfull'
    return JsonResponse({'message': message})