# VISTA obtain_route_fut
from .models import fut
from myapp_admin.models import ruta_tramite, notification, ticket_notififcation

def obtain_route_fut(id_fut):
	obj = fut.objects.filter(id=id_fut).values('route').first()
	return obj['route']

def obtain_tracking(id_fut):
	obj = ruta_tramite.objects.filter(fut_id_id=id_fut).values('tittle', 'name', 'reception', 'exit')
	# Convierte los resultados a una lista de diccionarios
	resultados_json = list(obj)
	return resultados_json

def update_notification(fut_id):
	# Obtén todos los objetos que tienen el mismo nombre
	objetos_a_actualizar = notification.objects.filter(fut_id_id = fut_id, view=False)
	
	# Itera sobre los objetos y actualiza el campo id_admin_turn y report_state
	for obj in objetos_a_actualizar:
		obj.view = True
		obj.save();
	return 'successfull'

def update_tickets(fut_id):
	# Obtén todos los objetos que tienen el mismo nombre
	objetos_a_actualizar = ticket_notififcation.objects.filter(fut_id_id = fut_id, view=False)
	
	# Itera sobre los objetos y actualiza el campo id_admin_turn y report_state
	for obj in objetos_a_actualizar:
		obj.view = True
		obj.save();
	return 'successfull'

def consult_fut_user(id_user):
	obj = fut.objects.filter(user_id_id=id_user).values('id', 'order', 'proceeding', 'date', 'finisher_state', 'code')
	# Convierte los resultados a una lista de diccionarios
	resultados_json = list(obj)
	return resultados_json

def consult_fut_user_2(id_user, finich_state):
	obj = fut.objects.filter(user_id_id=id_user, finisher_state=finich_state).values('id', 'order', 'proceeding', 'date', 'finisher_state', 'code')
	# Convierte los resultados a una lista de diccionarios
	resultados_json = list(obj)
	return resultados_json