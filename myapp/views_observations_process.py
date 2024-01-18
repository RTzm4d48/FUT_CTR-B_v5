from myapp_admin.models import ticket, ticket_desarrollo
from myapp.models import fut
from django.shortcuts import render

def obtain_tickets(id_fut):
	obj = ticket.objects.filter(fut_id_id=id_fut).values('tittle', 'charge')
	# Convierte los resultados a una lista de diccionarios
	print("tickets-----")
	print(obj)
	resultados_json = list(obj)

	return 'successfull'

def db_obtain_ticket(charge, fut_id):
	odj = None
	print("QUE PASA")
	if(charge == "alumno"):
		obj = ticket.objects.filter(charge='alumno', fut_id_id=fut_id, state=True).values('tittle', 'charge', 'code')
	else:
		obj = ticket.objects.exclude(charge='alumno').filter(fut_id_id=fut_id, state=True).values('tittle', 'charge', 'code')

	resultados_json = list(obj)
	return resultados_json

def obtain_id_ticket(code):
	obj = ticket.objects.filter(code=code).values('id', 'charge').first()
	return obj

def obtain_desarrollo_ticket(id_ticket):
	obj = ticket_desarrollo.objects.filter(ticket_id_id=id_ticket).values('id', 'name', 'desarrollo', 'charge', 'date')
	resultados_json = list(obj)
	return resultados_json

def obtain_data_ticket(id_ticket):
	obj = ticket.objects.filter(id=id_ticket).values('tittle', 'num_ticket', 'charge').first()
	return obj

def obtain_id_admin(fut_id):
	print("ESTAMOS OBTENIENDO LA ID DEL ADMIN")
	obj = fut.objects.filter(id=fut_id).values('id_admin_turn').first()
	return obj['id_admin_turn']

def create_ticket(user_name, charge, tittle, num_ticket, id_admin, id_fut, user_id):
	my_objet = ticket(name_creator=user_name, charge=charge, tittle=tittle, num_ticket=num_ticket, admin_id_id=id_admin, fut_id_id=id_fut, user_id_id=user_id)
	my_objet.save()
	new_id = my_objet.id
	new_num_ticket = my_objet.num_ticket

	new_data = {
	'id':new_id,
	'num_ticket': new_num_ticket
	}
	return new_data

def update_state_ticket(id_ticket, tittle):
	up_data = ticket.objects.get(id=id_ticket)
	up_data.state = True
	up_data.tittle = tittle
	up_data.save()
	return "successfull"

def insert_desarrollo(tittle, desarrollo, charge, date_format, id_ticket):
	my_objet = ticket_desarrollo(name=tittle, desarrollo=desarrollo, charge=charge, date=date_format, ticket_id_id=id_ticket)
	my_objet.save()
	new_id = my_objet.id
	return new_id




# TICKETS-----------------
def activated_ticket(ticket_id_db, titulo):
	#ACTUALIZAMOS EL STATE DEL MODELO ticket
	up_ticket = ticket.objects.get(id=ticket_id_db)
	up_ticket.state = True
	up_ticket.tittle = titulo
	up_ticket.save()
	return "successfull"

def insert_ticket_desarrollo(titulo, desarrollo, charge, date_format, ticket_id_db, img_binary_encoded):
	my_objet = ticket_desarrollo(name=titulo, desarrollo=desarrollo, charge=charge, date=date_format, ticket_id_id=ticket_id_db, img_attach=img_binary_encoded)
	my_objet.save()
	return 'successfull'

def random_num_ticket():
	num = 44445
	return num

def create_my_ticket(tittle, creator, charge, admin_id, fut_id, user_id):
	num_ticket = random_num_ticket()

	my_objet = ticket(name_creator=creator, charge=charge, tittle=tittle, num_ticket=num_ticket, admin_id_id=admin_id, fut_id_id=fut_id, user_id_id=user_id)
	my_objet.save()
	new_id = my_objet.id

	return new_id