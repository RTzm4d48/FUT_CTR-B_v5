from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
import base64

import json
from datetime import date, datetime

from myapp.views_observations_process import obtain_tickets
from myapp.views_observations_process import db_obtain_ticket
from myapp.views_observations_process import obtain_id_ticket
from myapp.views_observations_process import obtain_desarrollo_ticket
from myapp.views_observations_process import obtain_id_admin
from myapp.views_observations_process import create_ticket
from myapp.views_observations_process import update_state_ticket
from myapp.views_observations_process import insert_desarrollo

# TICKET
from myapp.views_observations_process import create_my_ticket
from myapp.views_observations_process import insert_ticket_desarrollo
from myapp.views_observations_process import activated_ticket
from myapp.views_observations_process import obtain_data_ticket

def init_observations(request):
	return render(request, 'view_fut/observations/observation_admin.html')

def tickets_path(request):
	return render(request, 'view_fut/observations/tickets.html')

def report_path(request):
	return render(request, 'view_fut/observations/report.html')

def redirect_show(request, code, charge):
	if code is None:
		return HttpResponse("<h1>404 ESTA PAGINA NO EXISTE :(</h1>")
	else:
		# CONSTRUIR LA URL
		send_path = 'n_show_path_2' if charge == 'alumno' else 'n_show_path'
		url_destino = reverse(send_path)+"?i="+code
		# REDIRIGIR A LA VISTA DESTINO
		return redirect(url_destino)

def show_path(request):
	code_input = request.GET.get('i')

	if code_input is None:
		return HttpResponse("<h1>404 ESTA PAGINA NO EXISTE :(</h1>")
	else:
		# OBTENER EL TITULO E ID DEL TICKET
		data_ticket = obtain_id_ticket(code_input)
		print("LOCURON_")
		print(data_ticket)
		return render(request, 'view_fut/observations/show.html', {
			'id_ticket': data_ticket['id'],
			'charge_ticket': data_ticket['charge']
		})

def get_db_ticket(request):
	if request.method == 'GET':
		charge = request.GET.get("charge")
		fut_id = request.GET.get("fut_id")

		data_obj = db_obtain_ticket(charge, fut_id)
		print(data_obj)

		return JsonResponse({'data': data_obj})
	else:
		return HttpResponse("<h1>404 Not Found :(</h1>")

# OBTENEMOS EL DESARROLLO DEL TICKET
def get_desarrollo_db(request):
	id_ticket = request.GET.get("id_ticket")
	# OBTENEMOS LOS DESARROLLOS DEL TICKET
	data_ticket = obtain_data_ticket(id_ticket)
	data_desarrollo = obtain_desarrollo_ticket(id_ticket)
	print(data_desarrollo)
	return JsonResponse({'data': data_desarrollo, 'only_this_ticket': data_ticket})


def update_desarrollo_ticket(request):
	if request.method == "POST":
		tittle = request.POST.get("tittle")
		desarrollo = request.POST.get("desarrollo")
		id_ticket = request.POST.get("id_ticket")
		desarrollo_type = request.POST.get("desarrollo_type")# PARA DIREFENCIAR DE UN NUEVO TICKET O YA EXISTENTE

		print("Datos recibidos")
		print(tittle)
		print(desarrollo)
		print(id_ticket)

		#obtener the date
		date_ = datetime.now()# output: 2023-11-21 15:24:10.832093
		date_format = date_.strftime("%Y-%m-%d %H:%M:%S")

		print("INSERT_TICKET_1")
		# HABILITAMOS EL TICKEET
		if(desarrollo_type == "new"):
			update_state_ticket(id_ticket, tittle)
		print("INSERT_TICKET_2")
		# INSERTAMOS EL DESARROLLO
		insert_desarrollo(tittle, desarrollo, '(alumno)', date_format, id_ticket)

		url_destino = reverse('n_tickets_path')
		# REDIRIGIR A LA VISTA DESTINO
		return redirect(url_destino)
	else:
		return HttpResponse("<h1>404 ESTA PAGINA NO EXISTE :(</h1>")

def create_user_ticket(request):
	if request.method == "GET":
		id_fut = request.GET.get("id_fut")
		num_ticket = request.GET.get("num_ticket")
		user_name = request.GET.get("user_name")
		user_id = request.GET.get("user_id")

		id_admin = obtain_id_admin(id_fut)# EL ID DEL ADMIN QUE TIENE EL FUT

		print("VACA2")
		new_data = create_ticket(user_name, 'alumno', 'null', num_ticket, int(id_admin), int(id_fut), int(user_id))
		print(new_data)
		return JsonResponse({'data': new_data})
	else:
		return HttpResponse("<h1>404 ESTA PAGINA NO EXISTE :(</h1>")


def crear_ticket(request):
	print("COMO? CHIQUITO BALDOBIA")
	# VARIABLES PARA CREAR TICKET
	tittle = request.POST.get('tittle')
	creator = request.POST.get('creator')
	charge = "alumno"
	fut_id = request.POST.get('fut_id')
	admin_id = obtain_id_admin(int(fut_id))# EL ID DEL ADMIN QUE TIENE EL FUT
	user_id = request.POST.get('user_id')
	# VARIABLES PARA DESARROLLO
	desarrollo = request.POST.get('desarrollo')
	#DATE
	date_ = datetime.now()
	date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
	# IMG
	if 'file_miImg' in request.FILES:
		img_file = request.FILES['file_miImg']
		img_binary = img_file.read()
		img_binary_encoded = base64.b64encode(img_binary)
	else:
		img_binary_encoded = b''# bynary bacio

	# mi_diccionario = {'tittle': tittle, 'creator': creator, 'charge': charge,
	# 'admin_id': admin_id, 'fut_id': fut_id, 'user_id': user_id, 'desarrollo': desarrollo}
	# print("TODAS LAS VARIABLES")
	# print(mi_diccionario)
	# print(img_binary_encoded)
	# print("LA IMAGEN")

	print("CREATE_TICKET_1")
	new_id_ticket = create_my_ticket(tittle, creator, charge, admin_id, fut_id, user_id)
	print("CREATE_TICKET_2")
	insert_ticket_desarrollo(tittle, desarrollo, charge, date_format, new_id_ticket, img_binary_encoded)
	print("CREATE_TICKET_3")
	activated_ticket(new_id_ticket, tittle);


	url_destino = reverse('n_tickets_path')
	# REDIRIGIR A LA VISTA DESTINO
	return redirect(url_destino)

def desarrollo_ticket(request):
	tittle = request.POST.get('tittle')
	desarrollo = request.POST.get('desarrollo')
	charge = "alumno"
	new_id_ticket = request.POST.get('id_ticket')
	#DATE
	date_ = datetime.now()
	date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
	# IMG
	if 'file_miImg_r' in request.FILES:
		img_file = request.FILES['file_miImg_r']
		img_binary = img_file.read()
		img_binary_encoded = base64.b64encode(img_binary)
	else:
		img_binary_encoded = b''# bynary bacio


	# mi_diccionario = {'tittle': tittle, 'desarrollo': desarrollo, 'new_id_ticket': new_id_ticket}
	# print("LOS DATOS DE DESARROLLO")
	# print(mi_diccionario)
	# print(img_binary_encoded)
	# print("LA IMGEN BYG")

	print("DESARROLLO INSERTADO")
	insert_ticket_desarrollo(tittle, desarrollo, charge, date_format, new_id_ticket, img_binary_encoded)

	url_destino = reverse('n_tickets_path')
	# REDIRIGIR A LA VISTA DESTINO
	return redirect(url_destino)