from myapp_admin.models import ticket, ticket_desarrollo, ticket_attach_file, ticket_url, ticket_notififcation

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