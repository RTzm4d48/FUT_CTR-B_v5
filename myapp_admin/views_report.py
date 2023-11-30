import base64
from django.http import HttpResponse, JsonResponse
from myapp_admin.models import Admins, reportes
from myapp.models import fut
from django.shortcuts import get_object_or_404

def create_report(request):
	menssage = request.GET.get('menssage')
	description = request.GET.get('description')
	fut_id = int(request.GET.get('fut_id'))
	admin_destino = request.GET.get('admin_destino')
	id_origen_admin = int(request.GET.get('id_origen_admin'))

	print("REPORT_01")
	id_destino_admin = obtain_id_admin_destination(admin_destino)

	print("REPORT_02")
	chanel_tourn_fut(fut_id, id_destino_admin)

	print("REPORT_03")
	id_report = generate_report(menssage, description, fut_id, id_destino_admin, id_origen_admin)

	return JsonResponse({'id_report': id_report})

# OBTENERMOS EL ADMIN_ID
def obtain_id_admin_destination(admin_destino):
	id_admin = Admins.objects.filter(position=admin_destino).values('id').first()
	return id_admin['id']

# GUARDAMOS EL REPORTE EN LA BD
def generate_report(menssage, description, fut_id, id_destino_admin, id_origen_admin):
	# Obtén una instancia válida del modelo fut, Admins
    fut_instance = get_object_or_404(fut, pk=fut_id)
    admin_instance = get_object_or_404(Admins, pk=id_origen_admin)
	#SAVE EN DB
    my_objet = reportes(menssage=menssage, description=description, fut_id=fut_instance, id_destino_admin=id_destino_admin, id_origen_admin=admin_instance)
    my_objet.save()
    new_id = my_objet.id
    return new_id

# MODIFICAMOS EL POSECIÓN DEL FUT (de quien lo posea)
def chanel_tourn_fut(fut_id, id_destino_admin):
	#ACTUALIZAMOS EL TURNO EN EL FUT
	up_fut = fut.objects.get(id=fut_id)
	up_fut.id_admin_turn = id_destino_admin
	up_fut.report_state = True
	up_fut.save()
	return "none"

# VISUALIZAR LOS FUTs REPORTADOS
def OBTAIN_REPORTS(id_admin):
	print("ESTAMOS EN OBTAIN REPORTS")
	# (/AQUÍ)(ESTO_SE_REPITE)
	obj_report = reportes.objects.filter(id_origen_admin=id_admin).values('menssage','description', 'fut_id_id')
	num_report_total = reportes.objects.filter(id_origen_admin=id_admin).count()

	#modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
	list_data = []
	for i in obj_report:
		diccionary={}
		diccionary['menssage'] = i['menssage'][:20]
		diccionary['description'] = i['description'][:40]
		diccionary['fut_id_id'] = i['fut_id_id']
		list_data.append(diccionary)

	return list_data, num_report_total

# SELECT REPORTS
def select_report(request):
	id_fut = request.GET.get('id_fut')
	id_destino_admin = request.COOKIES.get('id_admin')
	obj_report = obtain_report_view(id_fut, id_destino_admin)
	return JsonResponse(obj_report)

def obtain_report_view(id_fut, id_destino_admin):
	obj_report = reportes.objects.filter(fut_id_id=id_fut, id_destino_admin=id_destino_admin).values('menssage','description', 'id_origen_admin_id').first()
	return obj_report