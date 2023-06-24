import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
from myapp_admin.models import process, Admins, certificate

#para saber el dia y la hora actual
from datetime import datetime
from datetime import date


# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')


def log_verifying(log_position):
    # VARIABLES GENERALES
    #comprueb si la sesión esta iniciada
    Name_admin = 'none'
    Position_admin1 = 'none'
    Position_admin2 = 'none'
    
    # list_data = []
    diccionary={}
    
    if log_position == 'treasury' or log_position == 'secretary' or log_position == 'direction':

        objs = Admins.objects.filter(position=log_position).values('name', 'fullname').first()
        Name_admin = objs['name']
        diccionary['admin_name'] = Name_admin
            
        if log_position == 'treasury':
            diccionary['position_admin1'] = 'Tesorera'
            diccionary['position_admin2'] = 'Tesoreria' 
            diccionary['send_position'] = 'secretary'
            diccionary['stage_send'] = 1
        elif log_position == 'secretary':
            diccionary['position_admin1'] = 'Secretaria'
            diccionary['position_admin2'] = 'Secretaría' 
            diccionary['send_position'] = 'direction'
            diccionary['stage_send'] = 2
        else:
            diccionary['position_admin1'] = 'Director'
            diccionary['position_admin2'] = 'Dirección'
            diccionary['send_position'] = 'fut_finished'
            diccionary['stage_send'] = 3
            
            
        num_futs_total = fut.objects.exclude(stage__exact=3).filter(route=log_position).count()
        diccionary['num_futs'] = num_futs_total
        
        # list_data.append(diccionary)
        return diccionary

    else:
        #Mostramos la pagina de login
        #No borraremos la cookie por que no pude hacerlo :3
        return 'fail'

def staff_treasury(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    
    # (/AQUÍ)(ESTO_SE_REPITE)

    
    objs = fut.objects.exclude(stage__exact=3).filter(route=Position).values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')
    
    #names_short = [str(ob['order'])[:6] for ob in objs]
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    # Esto para saber cuantos fut's no esta leídos y el numero totoal de fut's
    num_no_view = 0
    total_futs = 0
    for i in objs:
        total_futs = total_futs + 1
        if i['view'] == 0:
            num_no_view = num_no_view + 1
    
    list_data = []
    num=1
    for i in objs:

        diccionary={}
        diccionary['id'] = i['id']
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        diccionary['stage'] = i['stage']
        diccionary['view'] = i['view']
        diccionary['num'] = num
        num = num + 1
        list_data.append(diccionary)
        
    return render(request, 'admin/staff_treasury.html', {
        'Object': list_data,
        'views': num_no_view,
        'total_futs': total_futs,
        #admin data
        'Data_log': Data_log
    })

def view_fut(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    # (/AQUÍ)(ESTO_SE_REPITE)

    code_ = request.GET.get('code')
    # el 'mode' es para determinar que botones mostrar
    mode = request.GET.get('mode')

    objs = fut.objects.filter(code=code_).values('id', 'myrequest', 'name', 'program', 'phone', 'dni', 'cycle', 'reason', 'email', 'order', 'date').first()

    # actualizamos el campo view
    up_register = fut.objects.get(code=code_)
    up_register.view = 1
    up_register.save()

    return render(request, 'admin/staff/view_fut.html', {
        'code': code_,
        'objs': objs,
        'mode': mode,
        'position': Position,
        'Data_log': Data_log
    })

def save_my_certifcate(tittle_, pdf_binary_, state_, fut_id_):
    my_objs = certificate(tittle=tittle_, pdf_binary=pdf_binary_, state=state_, fut_id_id=fut_id_)
    my_objs.save()
    new_id = my_objs.id
    return new_id


def send_inssued(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    
    # (/AQUÍ)(ESTO_SE_REPITE)

    
    objs = fut.objects.exclude(stage__exact=3).filter(route=Position).values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')
    
    #names_short = [str(ob['order'])[:6] for ob in objs]
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    # Esto para saber cuantos fut's no esta leídos y el numero totoal de fut's
    num_no_view = 0
    total_futs = 0
    for i in objs:
        total_futs = total_futs + 1
        if i['view'] == 0:
            num_no_view = num_no_view + 1
    
    list_data = []
    num=1
    for i in objs:

        diccionary={}
        diccionary['id'] = i['id']
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        diccionary['stage'] = i['stage']
        diccionary['view'] = i['view']
        diccionary['num'] = num
        num = num + 1
        list_data.append(diccionary)

    # APARTIR DE QUI EMPIEZA EL PROCESO DE 'SEND INSSUED'
    fut_id = request.POST.get('fut_id')
    fut_tittle = request.POST.get('fut_tittle')

    # Ahora Haremos el proceso de 'Send Definitivo'
    #obtenemos la cookie para realizar el proceso de envio
    Position = request.COOKIES.get('log_position')
    message = send_definity('none', fut_id, Position)
    # Fin del 'Send Defintivo'
    print('NI PAPASSS')
    # my_pdf = request.POST.get('my_pdf')
    archivo_pdf = request.FILES['my_pdf']
    contenido_bytes = archivo_pdf.read()
    pdf_binary_encoded = base64.b64encode(contenido_bytes)

    save_my_certifcate(fut_tittle, pdf_binary_encoded, 0, fut_id)
    
    return render(request, 'admin/staff_treasury.html', {
        'Object': list_data,
        'views': num_no_view,
        'total_futs': total_futs,
        #admin data
        'Data_log': Data_log
    })

def view_send(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        stage_ = request.GET.get('stage')

        #actualizamos el campo stage del modelo fut
        up_register = fut.objects.get(id=id)
        up_register.stage = stage_
        up_register.save()

        # Hacer algo con la variable 'var'
        return HttpResponse('Variable recibida: ' + id)
    
def postulated(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    
    # (/AQUÍ)(ESTO_SE_REPITE)

    objs = fut.objects.filter(stage=1, route=Position).values('order', 'reason', 'name', 'dni', 'code')

    
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        list_data.append(diccionary)
        
    return render(request, 'admin/staff/postulated.html', {
        'Object': list_data,
        'Data_log': Data_log
    })
def pending(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    # (/AQUÍ)(ESTO_SE_REPITE)

    objs = fut.objects.filter(stage=2).values('order', 'reason', 'name', 'dni', 'code')

    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        list_data.append(diccionary)
        
    return render(request, 'admin/staff/pending.html', {
        'Object': list_data,
        'Data_log': Data_log
    })

def send(request):
    # Validacion de cookies y validacion de usuario (AQUÍ)(ESTO_SE_REPITE)
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
  
    Data_log = log_verifying(Position)
    
    if login == None:
        return render(request, 'ils_admin.html')
    elif Data_log == 'fail':
        return render(request, 'ils_admin.html')
    # (/AQUÍ)(ESTO_SE_REPITE)
    objs = fut.objects.filter(route=Data_log['send_position']).values('id','order', 'reason', 'name', 'dni', 'code')

    #OBTENDREMOS LA FECHA DE ENVIO
    id_fut = 0
    for i in objs:
        id_fut = i['id']
    objs2 = process.objects.filter(fut_id_id=id_fut, stage=Data_log['stage_send']).values('exit').first()
    fecha_str = str(objs2['exit'])
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S%z')
    fecha_compacta = fecha.strftime('%Y-%m-%d %H:%M:%S')

    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        diccionary['date_exit'] = fecha_compacta
        list_data.append(diccionary)

    return render(request, 'admin/staff/send.html', {
        'Object': list_data,
        'Data_log':Data_log
    })

def name_admin(position):
    if position == 'treasury' or position == 'secretary' or position == 'direction':
        if position == 'treasury':
            next_position = 'secretary'
        elif position == 'secretary':
            next_position = 'direction'
        else:
            next_position = 'finisher'
        objs = Admins.objects.filter(position=next_position).values('name', 'fullname').first()
        name = objs['name']+' '+objs['fullname']
        return name
    else:
        return 'fail'

def save_process(tittle, name, reception, exit, state, num, fut_id, stage):
    my_objet = process(tittle = tittle, name = name, reception = reception, exit = exit, state = state, num = num, fut_id_id = fut_id, stage = stage)
    my_objet.save()
    new_id = my_objet.id
    return new_id

def send_definity(ticket, id, Position):
    #variables constantes
    send_position = 'none'
    route_send = 'none'
    stage = 0
    num = 0

    print("PASAMOS POR SEND DEFINITY")
    if Position == 'treasury':
        send_position = 'secretary'
        route_send = 'SECRETARIA'
        stage = 2
        num = 60
    elif Position == 'secretary':
        send_position = 'direction'
        route_send = 'DIRECCION'
        stage = 3
        num = 80
    else:
        send_position = 'send_exit'
        route_send = 'TRAMITE REALIZADO'
        stage = 4
        num = 100

    #actualizamos los datos de 'FUT'
    up_register = fut.objects.get(id=id)
    if Position == 'treasury':
        up_register.n_ticket = ticket
    up_register.route = send_position
    up_register.stage = 0
    up_register.view = 0
    up_register.save()

    #obtener the date
    date = datetime.now() 
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")

    #Actualizamos los datos de 'admin_process'
    bef_stage = stage - 1
    print(bef_stage)
    print(id)
    up_process_2 = process.objects.get(stage=bef_stage, fut_id_id=id)
    up_process_2.exit = date_format
    up_process_2.save()
    print('GUARDAMOS EL PROCESO PA')
    #Insert in the BD
    admin_name = name_admin(Position)
    new_id = save_process(route_send, admin_name, date_format, None, False, num, id, stage)

    message = 'successful'
    return message

def send_01_treasurer(request):
    #obtenemos la cookie para realizar el proceso de envio
    Position = request.COOKIES.get('log_position')

    ticket = request.GET.get('ticket')
    id = request.GET.get('id')
    message = send_definity(ticket, id, Position)
    return JsonResponse({'message': message})

def admin_login(request):
    theposition = request.GET.get('position')
    theemail = request.GET.get('email')
    thepass = request.GET.get('thepass')

    #Consultamos el modelo de 'admins'
    objs_email = Admins.objects.filter(position=theposition, email=theemail).values('id').first()
    objs_pass = Admins.objects.filter(position=theposition, email=theemail, password=thepass).values('id').first()

    #validamos el login
    answer = {}
    if objs_email == None:
        answer = {'status': 'Email incorrecto'}
    else:
        if objs_pass == None:
            answer = {'status': 'Contraseña incorrecta'}
        else:
            answer = {'status': 'success'}
            # Creamos la cookie
            response = JsonResponse(answer)
            response.set_cookie('log_admin', 'true')
            response.set_cookie('log_position', theposition)
            return response
    
    return JsonResponse(answer)