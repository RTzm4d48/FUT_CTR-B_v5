from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

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
	data_desarrollo = obtain_desarrollo_ticket(id_ticket)
	print(data_desarrollo)
	return JsonResponse({'data': data_desarrollo})


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