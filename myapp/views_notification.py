import base64
from django.http import JsonResponse
from myapp_admin.models import notification
from myapp_admin.models import ticket_notififcation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import fut

# @method_decorator(login_required, name='dispatch')
def get_message_ticket(request):
    # Verificar si el usuario está autenticado
	if request.user.is_authenticated:
        # Obtener la ID del usuario autenticado
		user_id = request.user.id
		
		myobj = obtain_tickets(user_id);

		return JsonResponse({'data':myobj})
	else:
		return JsonResponse({'data':None})

def get_notification(request):
	# Verificar si el usuario está autenticado
	if request.user.is_authenticated:
        # Obtener la ID del usuario autenticado
		user_id = request.user.id

		# OBTENRMOS LA NOTIFIACIÓN
		my_obj = obtain_data(user_id)

		return JsonResponse({'data':my_obj})
	else:
		return JsonResponse({'data':None})

def obtain_data(id_user):
	my_obj = notification.objects.filter(user_id_id=id_user).values('tittle', 'date', 'tipo', 'view', 'fut_id_id', 'emitido')[::-1]
	# Convierte los resultados a una lista de diccionarios
	resultados_json = list(my_obj)
	return resultados_json

def obtain_tickets(id_user):
	my_obj = ticket_notififcation.objects.filter(user_id_id=id_user).values('tittle', 'desarrollo', 'date','emitido','charge','view','fut_id_id')[::-1]
	# Convierte los resultados a una lista de diccionarios
	resultados_json = list(my_obj)
	return resultados_json

# OBTENEMOS EL CODIGO DEL FUT
def open_fut(request):
	id_fut = request.GET.get('id_fut')
	my_obj = fut.objects.filter(id=id_fut).values('code').first()
	return JsonResponse({'data':my_obj})