from django.http import JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from myapp.views_view_fut_process import obtain_route_fut
from myapp.views_view_fut_process import obtain_tracking
from myapp.views_view_fut_process import update_notification
from myapp.views_view_fut_process import update_tickets
from myapp.views_view_fut_process import consult_fut_user
from myapp.views_view_fut_process import consult_fut_user_2

def tracking(request):
	id_fut = request.GET.get('id_fut')
	obj = obtain_tracking(id_fut)# OBTENEMOS LOS DETALLES DE SEGUIMIENTO
	return JsonResponse({'data': obj})

def pros_route(request):
	id_fut = request.GET.get('id_fut')
	route = obtain_route_fut(id_fut)# OBTENEMOS LA RUTA EN LA QUE SE ENCUENTRA EL FUT
	return JsonResponse({'route':route})

# ACTUALIZAR EL VIEW DE LAS NOTIFICACIONES
def view_fut(request):
	id_fut = request.GET.get('id_fut')
	print('UPDATE_1')
	update_notification(id_fut)
	print('UPDATE_2')
	update_tickets(id_fut)

	return JsonResponse({'data':'successfull'})

@login_required
def fut_all(request):
	return render(request, 'view_fut/futs/futs.html')

def fut_finish(request):
	return render(request, 'view_fut/futs/finished.html')

def  fut_process(request):
	return render(request, 'view_fut/futs/in-progress.html')

def fut_consult(request):
	id_user = request.GET.get('user_id')
	allOrOne = request.GET.get('allOrOne')
	finich_state = request.GET.get('finich_state')

	# los datos recibidos con post se reciben como strem, asi que creo una nueva varable boolean
	state = 1 if finich_state == "true" else 0;

	if(allOrOne == "all"):
		data = consult_fut_user(id_user)
	else:
		data = consult_fut_user_2(id_user, state)

	return JsonResponse({'data': data})