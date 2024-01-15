import base64
from django.http import HttpResponse, JsonResponse
from myapp_admin.models import ticket, ticket_desarrollo, ticket_attach_file, ticket_url, ticket_notififcation
from datetime import datetime

#pip install qrcode

def create_ticket(request):
	titulo = request.GET.get('titulo')
	desarrollo = request.GET.get('desarrollo')
	creator = request.GET.get('creator')
	state = request.GET.get('state')
	charge = request.GET.get('charge')
	num_ticket = request.GET.get('num_ticket')
	admin_id = request.GET.get('admin_id');
	fut_id = request.GET.get('fut_id');
	user_id = request.GET.get('user_id')

	#SAVE EN DB
	my_objet = ticket(name_creator=creator, charge=charge, tittle=titulo, num_ticket=num_ticket, admin_id_id=admin_id, fut_id_id=fut_id, user_id_id=user_id)
	my_objet.save()
	new_id = my_objet.id
	return JsonResponse({'the_id_ticket': new_id})

def activated_ticket(ticket_id_db, titulo):
	#ACTUALIZAMOS EL STATE DEL MODELO ticket
	up_ticket = ticket.objects.get(id=ticket_id_db)
	up_ticket.state = True
	up_ticket.tittle = titulo
	up_ticket.save()
	return "successfull"

def insert_ticket_notififcation(name,desarrollo,date,name_admin,charge_admin,id_fut,user_id):
	my_obt = ticket_notififcation(tittle=name,desarrollo=desarrollo,date=date,emitido=name_admin,charge=charge_admin,fut_id_id=id_fut,user_id_id=user_id)
	my_obt.save()
	return "successfull"

def insert_ticket_desarrollo(titulo, desarrollo, charge, date_format, ticket_id_db):
	my_objet = ticket_desarrollo(name=titulo, desarrollo=desarrollo, charge=charge, date=date_format, ticket_id_id=ticket_id_db)
	my_objet.save()
	return 'successfull'

def update_desarrollo(request):
    titulo = request.GET.get('titulo')
    desarrollo = request.GET.get('desarrollo')
    charge = request.GET.get('charge')
    #DATE
    date_ = datetime.now() 
    date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
    ticket_id_db = request.GET.get('ticket_id_db')
    #NEW DATES
    name_admin = request.GET.get('name_admin')
    chargeAdmin = request.GET.get('chargeAdmin')
    fut_id = request.GET.get('fut_id')
    user_id = request.GET.get('user_id')

    print(name_admin)
    print(chargeAdmin)
    print(fut_id)
    print(user_id)

    print("SAVE_TICKET_1")
    insert_ticket_desarrollo(titulo, desarrollo, charge, date_format, ticket_id_db)
    print("SAVE_TICKET_2")
    activated_ticket(ticket_id_db, titulo);
    print("SAVE_TICKET_3")
    insert_ticket_notififcation(titulo,desarrollo,date_format,name_admin,chargeAdmin,fut_id,user_id)

    return JsonResponse({'message': 'successfull'})

def loading_ticket(request):
	my_id = request.GET.get('id_fut');
	print("LA IDE ES ESTO: "+ str(my_id))
	num_registros = ticket.objects.filter(fut_id_id=my_id, state=True).count()
	print("NUM TICKETS: "+ str(num_registros))

	resultados = ticket.objects.filter(fut_id_id=my_id, state=True).values('id', 'tittle', 'admin_id_id', 'num_ticket', 'name_creator')[:num_registros]
    # Convierte los resultados a una lista de diccionarios
	resultados_json = list(resultados)
	if(resultados_json == []):
		print("Bacio")

	#print(str(resultados[0]['num_ticket']))
	
	
	return JsonResponse({'tickets': resultados_json, 'num_registros': num_registros})

def moreloading_ticket(request):
	id_ticket = request.GET.get('id_ticket')
	# AQUI OBTENEMOS LOS DATOS DEL MODELO DESARROLLO
	print("TICKET DESARROLLO");
	desarrollo = ticket_desarrollo.objects.filter(ticket_id_id=id_ticket).values('name', 'desarrollo', 'charge', 'date')#.first()
	resultados_json = list(desarrollo)

	return JsonResponse({'more_tickets':resultados_json})