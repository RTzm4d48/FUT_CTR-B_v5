from myapp.models import fut
import base64
from django.conf import settings
import os

# OBTENEMOS LA IMG DE PAGO Y LA ESCRIBIMOS EN LA CARPETA tmp
def manage_img(fut_id):
    objs = fut.objects.filter(id=fut_id).values('img_pay').first()
    # print(objs)
    #print('--orsok--')
    pdf_binary = base64.b64decode(objs['img_pay'])
    #print(pdf_binary)
    #print('--orslok_platano-aja-')

    #ruta_guardar_pdf = 'myapp_admin/static/tmp/pay_photo_'+fut_id+'.jpg'
    ruta_guardar_pdf = os.path.join(settings.STATIC_ROOT, 'tmp', f'pay_photo_{fut_id}.jpg')

    with open(ruta_guardar_pdf, 'wb') as output_pdf:
        output_pdf.write(pdf_binary)

    return "successfull"
