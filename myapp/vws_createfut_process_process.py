import base64
import os
from django.conf import settings

def paint_qr_img(user_id, qrimg_binary):
	img_binary = base64.b64decode(qrimg_binary)
	name_file = 'tmp\img_'+str(user_id)+'_qr.jpg'

	ruta_guardar_img = os.path.join(settings.STATIC, name_file)
	print(ruta_guardar_img)

	with open(ruta_guardar_img, 'wb') as output_img:
		output_img.write(img_binary)

	return 'successfull'