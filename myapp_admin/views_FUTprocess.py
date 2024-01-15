from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

import base64

# para descargar una imagen
from django.conf import settings
import os

from myapp_admin.views_FUTprocess_process import next_admin
from myapp_admin.views_FUTprocess_process import update_fut
from myapp_admin.views_FUTprocess_process import insert_tracking
from myapp_admin.views_FUTprocess_process import update_route_exit
from myapp_admin.views_FUTprocess_process import insert_notification
from myapp_admin.views_FUTprocess_process import save_process_secretary
from myapp_admin.views_FUTprocess_process import save_public_direction
from myapp_admin.views_FUTprocess_process import manage_document

def process_fut(request):
	fut_id = request.GET.get("fut_id")
	admin_id = request.GET.get("admin_id")
	user_id = request.GET.get("user_id")
	route = request.GET.get("route");
	num_boleta = request.GET.get("num_boleta");

	print('FUTprocess_01')
	id_next_admin = next_admin(admin_id)
	print('FUTprocess_02')
	#ACTUALIZAR EL CAMPO EXIT DE LA RUTA
	update_route_exit(fut_id);
	print('FUTprocess_03')
	update_fut(fut_id, id_next_admin, route, num_boleta)
	print('FUTprocess_04')
	insert_tracking(fut_id, admin_id, id_next_admin)
	print('FUTprocess_05')
	insert_notification('Procesado', admin_id, fut_id, user_id)

	success_url = reverse("n_staff_treasury")
	return HttpResponseRedirect(success_url)

def write_myFile(request):
	if request.method == 'POST':
		archivo = request.FILES['file_pdf']
		description = request.POST.get("description")

		print(description)

	return JsonResponse({'message': 'successfull'})

def secretary_process_doc(request):
	if request.method == 'POST':
		coment = request.POST.get("secretary_descript")
		fut_id = request.POST.get("fut_id_s")
		order = request.POST.get("order_s")

		# VARIABLES PARA process_fut
		admin_id = request.POST.get("admin_id_s")
		user_id = request.POST.get("user_id_s")
		route = "direction";
		num_boleta = "None";

		# Validando si se envio el pdf
		if 'file_pdf' in request.FILES:
			file_pdf = request.FILES['file_pdf']
			pdf_binary = file_pdf.read()
			pdf_binary_encoded = base64.b64encode(pdf_binary)
		else:
			pdf_binary_encoded = b''# bynary bacio

		print("SAVE SECRETARY PROCESS")
		save_process_secretary(order, pdf_binary_encoded, coment, fut_id)
		print("NOS REDIRECCIONAMOS A OTRA VISTA PARA PROCESAR FUT")
		success_url = reverse("n_process_fut") + f'?fut_id={fut_id}&admin_id={admin_id}&user_id={user_id}&route={route}&num_boleta={num_boleta}'
		print(success_url)
		return HttpResponseRedirect(success_url)
	else:
		return HttpResponse("<h1>404 Not Found :(</h1>")

def direction_process_doc(request):
	if request.method == 'POST':
		num_expediente = request.POST.get("num_expediente")
		select_pdf_direction = request.POST.get("select_pdf_direction")
		fut_id = request.POST.get("fut_id_d")
		order = request.POST.get("order_d")

		# VARIABLES PARA process_fut
		admin_id = request.POST.get("admin_id_d")
		user_id = request.POST.get("user_id_d")
		route = "finished";
		num_boleta = "None";

		# Validando si se envio el pdf
		if 'file_direction' in request.FILES:
			file_pdf = request.FILES['file_direction']
			pdf_binary = file_pdf.read()
			pdf_binary_encoded = base64.b64encode(pdf_binary)
		else:
			pdf_binary_encoded = b''# bynary bacio

		print("SAVE DIRECTION PUBLIC")
		save_public_direction(num_expediente, fut_id, order, pdf_binary_encoded)
		print("NOS REDIRECCIONAMOS A OTRA VISTA PARA PROCESAR FUT")
		success_url = reverse("n_process_fut") + f'?fut_id={fut_id}&admin_id={admin_id}&user_id={user_id}&route={route}&num_boleta={num_boleta}'
		print(success_url)
		return HttpResponseRedirect(success_url)
	else:
		return HttpResponse("<h1>404 Not Found :(</h1>")

# PARA ESCRIBIR EL DOCUMENTO EN media
def download_doc(request):
	if request.method == 'GET':
		fut_id = request.GET.get("id_fut")
		
		# OBTENEMOS EL DOCUMENTO Y LO ESCRIBIMOS EN LA CARPETA media
		manage_document(fut_id)
		return JsonResponse({'message': 'successfull'})
	else:
		return HttpResponse("<h1>404 Not Found :(</h1>")

# ESTA FUNCIÓN FINALMENTE DESCARGA EL ARCHIVO
def direct_download(request):
	if request.method == 'GET':
		fut_id = request.GET.get('fut_id')

		file = 'doc_tramited_fut_'+fut_id+'.pdf'
		file_path = os.path.join(settings.MEDIA_ROOT_ADMIN, file)

		try:
			with open(file_path, 'rb') as f:
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