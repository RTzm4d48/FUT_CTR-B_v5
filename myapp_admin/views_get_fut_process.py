from myapp.models import fut
import base64

# OBTENEMOS LA IMG DE PAGO Y LA ESCRIBIMOS EN LA CARPETA tmp
def manage_img(fut_id):
    objs = fut.objects.filter(id=fut_id).values('img_pay').first()
    # print(objs)
    pdf_binary = base64.b64decode(objs['img_pay'])

    ruta_guardar_pdf = 'myapp_admin/static/tmp/pay_photo_'+fut_id+'.jpg'

    with open(ruta_guardar_pdf, 'wb') as output_pdf:
        output_pdf.write(pdf_binary)

    return "successfull"