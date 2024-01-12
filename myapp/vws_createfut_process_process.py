import base64
import os
from django.conf import settings

from myapp_admin.models import direction_public_document

def paint_qr_img(user_id, qrimg_binary):
	img_binary = base64.b64decode(qrimg_binary)
	name_file = 'tmp\img_'+str(user_id)+'_qr.jpg'

	ruta_guardar_img = os.path.join(settings.STATIC, name_file)
	print(ruta_guardar_img)

	with open(ruta_guardar_img, 'wb') as output_img:
		output_img.write(img_binary)

	return 'successfull'


def manage_document(fut_id):
	objs = direction_public_document.objects.filter(fut_id_id=fut_id).values('tittle', 'the_file', 'expediente').first()
	pdf_binary = base64.b64decode(objs['the_file'])
	name_file = 'doc_finisher_tramited_fut_'+fut_id+'.pdf'
	ruta_guardar_pdf = os.path.join(settings.MEDIA_ROOT, name_file)

	with open(ruta_guardar_pdf, 'wb') as output_pdf:
		output_pdf.write(pdf_binary)

	lista = {'tittle': objs['tittle'], 'expediente': objs['expediente']}
	return lista

