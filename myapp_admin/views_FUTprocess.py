from django.http import JsonResponse

from myapp_admin.views_FUTprocess_process import next_admin
from myapp_admin.views_FUTprocess_process import update_fut
from myapp_admin.views_FUTprocess_process import insert_tracking
from myapp_admin.views_FUTprocess_process import update_route_exit
from myapp_admin.views_FUTprocess_process import insert_notification

def process_fut(request):
	message = 'sussesfull'
	fut_id = request.GET.get("fut_id")
	admin_id = request.GET.get("admin_id")
	user_id = request.GET.get("user_id")

	print('FUTprocess_01')
	id_next_admin = next_admin(admin_id)
	print('FUTprocess_02')
	#ACTUALIZAR EL CAMPO EXIT DE LA RUTA
	update_route_exit(fut_id);
	print('FUTprocess_03')
	update_fut(fut_id, id_next_admin)
	print('FUTprocess_04')
	insert_tracking(fut_id, admin_id, id_next_admin)
	print('FUTprocess_05')
	insert_notification('Procesado', admin_id, fut_id, user_id)


	return JsonResponse({'message': 'successfull'})
