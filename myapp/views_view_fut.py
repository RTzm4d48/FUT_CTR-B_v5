from django.http import JsonResponse

from myapp.views_view_fut_process import obtain_route_fut
from myapp.views_view_fut_process import obtain_tracking
from myapp.views_view_fut_process import update_notification
from myapp.views_view_fut_process import update_tickets

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