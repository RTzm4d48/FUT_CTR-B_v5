from myapp.models import fut
from myapp_admin.models import Admins, ruta_tramite, notification
from datetime import date, datetime

def insert_tracking(fut_id, admin_id, id_next_admin):
	obj = Admins.objects.filter(id=id_next_admin).values('name', 'fullname', 'position').first()
	
	# INTEGRAMOS EN NAME
	name = obj['name']+' '+obj['fullname']

	#obtener the date
	mydate = datetime.now()# output: 2023-11-21 15:24:10.832093
	date_format = mydate.strftime("%Y-%m-%d %H:%M:%S")

    #COVERTIR LA POSICIÓN A MAYUSCULAS
	tittle = obj['position'].upper()

	save_process(tittle, name, date_format,fut_id)
	return 'successfull'

#@sync_to_async
def save_process(tittle, name, reception, fut_id):
    my_objet = ruta_tramite(tittle = tittle, name = name, reception = reception, fut_id_id = fut_id)
    my_objet.save()
    return "successfull"

# OBTENEMOS EL PUESTO DEL SEGUIENTE ADMIN
def next_admin(admin_id):
	obj = Admins.objects.values('id', 'position')
	
	position = Position_my_admin(admin_id, obj)

	if position == "treasury":
		return get_next_admin('secretary', obj)
	elif position == "secretary":
		return get_next_admin('direction', obj)
	else:
		return 0;# EL FUT YA NO PERTENECE A NINGUN ADMIN (por que ya proceso direccion)(esta finalizado)

# OBTENEMOS LA POSICIÓN DEL ADMIN ACTUAL
def Position_my_admin(admin_id, obj):
	for i in obj:
		print("itaracion: "+ str(i['id']))# OUTPUT: itaracion: {'id': 1, 'position': 'treasury'}
		if(i['id'] == int(admin_id)):
			return i['position']
	return 'fail'

# OBTEBEMOS LA ID DEL PROXIMO ADMIN
def get_next_admin(next_charge, obj):
	for i in obj:
		if i['position'] == next_charge:
			return i['id']
	return 'fail'

# ACTUALIZAMOS LA TABLA FUT
def update_fut(fut_id, new_rute):
	up_data = fut.objects.get(id=fut_id)
	up_data.id_admin_turn = new_rute
	up_data.report_state = False
	up_data.save()
	return "successfull"

#ACTUALIZAR EL CAMPO EXIT DE LA RUTA
def update_route_exit(fut_id):

	#obtener the date
	mydate = datetime.now()# output: 2023-11-21 15:24:10.832093
	date_format = mydate.strftime("%Y-%m-%d %H:%M:%S")

	# Obtén todos los objetos que tienen el mismo nombre
	objetos_a_actualizar = ruta_tramite.objects.filter(exit=None, fut_id_id=fut_id)
	
	# Itera sobre los objetos y actualiza el campo id_admin_turn y report_state
	for obj in objetos_a_actualizar:
		print(obj)
		obj.exit = date_format
		obj.save();

	return 'successfull'

def obtain_tipe(admin_id):
	obj = Admins.objects.filter(id=admin_id).values('name', 'position').first()
	return obj

def insert_notification(tittle, admin_id, fut_id, user_id):
	#obtener the date
	mydate = datetime.now()# output: 2023-11-21 15:24:10.832093
	date_format = mydate.strftime("%Y-%m-%d %H:%M:%S")

	date_admin = obtain_tipe(admin_id);
	print(date_admin['name'])
	print(date_admin['position'])
	emitido = date_admin['position']
	tipo = "Procesado por - "+date_admin['name']

	my_objet = notification(tittle = tittle, date = date_format, emitido = emitido, tipo = tipo, fut_id_id=fut_id, user_id_id=user_id)
	my_objet.save()

	return 'successfull'
