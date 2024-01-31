import base64
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from myapp_admin.models import ticket, ticket_desarrollo, ticket_attach_file, ticket_url, ticket_notififcation
from datetime import datetime

from django.urls import reverse

from myapp_admin.views_tickets_process import activated_ticket
from myapp_admin.views_tickets_process import insert_ticket_notififcation
from myapp_admin.views_tickets_process import insert_ticket_desarrollo
from myapp_admin.views_tickets_process import create_my_ticket
from myapp_admin.views_tickets_process import insert_ticket_desarrollo

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

    print("SAVE_TICKET_1")
    insert_ticket_desarrollo(titulo, desarrollo, charge, date_format, ticket_id_db)
    print("SAVE_TICKET_2")
    activated_ticket(ticket_id_db, titulo);
    print("SAVE_TICKET_3")
    insert_ticket_notififcation(titulo,desarrollo,date_format,name_admin,chargeAdmin,fut_id,user_id)

    return JsonResponse({'message': 'successfull'})

def prueba(request):
	# VARIABLES PARA VOLVER A SHOW_FUT
	code = request.POST.get('code')
	mode = request.POST.get('mode')
	# VARIABLES PARA CREAR TICKET
	tittle = request.POST.get('tittle')
	creator = request.POST.get('creator')
	charge = request.POST.get('charge')
	admin_id = request.POST.get('admin_id')
	fut_id = request.POST.get('fut_id')
	user_id = request.POST.get('user_id')
	# VARIABLES PARA DESARROLLO
	desarrollo = request.POST.get('desarrollo')
	# pdf_file_miImg = request.POST.get('pdf_file_miImg')
	#DATE
	date_ = datetime.now()
	date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
	# IMG
	if 'pdf_file_miImg' in request.FILES:
		img_file = request.FILES['pdf_file_miImg']
		img_binary = img_file.read()
		img_binary_encoded = base64.b64encode(img_binary)
	else:
		img_binary_encoded = b''# bynary bacio


	# mi_diccionario = {'code': code, 'mode': mode, 'tittle': tittle, 'creator': creator, 'charge': charge,
	# 'admin_id': admin_id, 'fut_id': fut_id, 'user_id': user_id, 'desarrollo': desarrollo}
	# print("TODAS LAS VARIABLES")
	# print(mi_diccionario)

	print("CREATE_TICKET_1")
	new_id_ticket = create_my_ticket(tittle, creator, charge, admin_id, fut_id, user_id)
	print("CREATE_TICKET_2")
	insert_ticket_desarrollo(tittle, desarrollo, charge, date_format, new_id_ticket, img_binary_encoded)
	print("CREATE_TICKET_3")
	activated_ticket(new_id_ticket, tittle);
	print("CREATE_TICKET_4")
	insert_ticket_notififcation(tittle, desarrollo, date_format, creator, charge, fut_id, user_id)


	print("NOS REDIRECCIONAMOS A OTRA VISTA DE SHOW FUT")
	success_url = reverse("n_view_fut") + f'?code={code}&mode={mode}'
	print(success_url)

	return HttpResponseRedirect(success_url)

def observation_reply(request):
	# VARIABLES PARA VOLVER A SHOW_FUT
	code = request.POST.get('code')
	mode = request.POST.get('mode')

	# DATA
	tittle = request.POST.get('tittle_r')
	desarrollo = request.POST.get('desarrollo_r')
	charge = request.POST.get('charge_r')
	new_id_ticket = request.POST.get('ticket_id')
	# DATE
	date_ = datetime.now()
	date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
	# IMG
	if 'file_miImg_r' in request.FILES:
		img_file = request.FILES['file_miImg_r']
		img_binary = img_file.read()
		img_binary_encoded = base64.b64encode(img_binary)
	else:
		img_binary_encoded = b''# bynary bacio

	print("ESTAMOS EMN REPLY")
	# mi_diccionario = {'tittle': tittle, 'desarrollo': desarrollo, 'new_id_ticket': new_id_ticket, 'charge': charge}
	# print("LOS DATOS DE DESARROLLO")
	# print(mi_diccionario)
	# print(img_binary_encoded)
	# print("LA IMGEN BYG")

	print("INSERTANDO DESARROLLO")
	insert_ticket_desarrollo(tittle, desarrollo, charge, date_format, new_id_ticket, img_binary_encoded)

	print("NOS REDIRECCIONAMOS A OTRA VISTA DE SHOW FUT")
	success_url = reverse("n_view_fut") + f'?code={code}&mode={mode}'
	print(success_url)
	return HttpResponseRedirect(success_url)

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
	desarrollo = ticket_desarrollo.objects.filter(ticket_id_id=id_ticket).values('id','name', 'desarrollo', 'charge', 'date')#.first()
	resultados_json = list(desarrollo)
	# print(resultados_json)
	return JsonResponse({'more_tickets':resultados_json})

def get_img_attach(id_ticket):
	desarrollo = ticket_desarrollo.objects.filter(ticket_id_id=id_ticket).values('id','img_attach')

	for i in desarrollo:
		print("ITERANDO_IMG")
		if(i['img_attach'] != b''):
			# ESCRIBIENDO LA IMGEN
			img_binary = base64.b64decode(i['img_attach'])
			ruta_guardar_img = 'myapp_admin/static/tmp/desarrollo_attach_'+str(i['id'])+'.jpg'
			with open(ruta_guardar_img, 'wb') as output_img:
				output_img.write(img_binary)
	return 'successfull'

def all_desarrollo_data(request):
	id_ticket = request.GET.get('id_ticket')
	# AQUI OBTENEMOS LOS DATOS DEL MODELO DESARROLLO
	get_img_attach(id_ticket)
	desarrollo = ticket_desarrollo.objects.filter(ticket_id_id=id_ticket).values('id','name', 'desarrollo', 'charge', 'date')#.first()
	resultados_json = list(desarrollo)
	# print(resultados_json)
	return JsonResponse({'more_tickets':resultados_json})