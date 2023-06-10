from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
from myapp_admin.models import process, Admins

#para saber el dia y la hora actual
from datetime import datetime
from datetime import date


# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')


def log_verifying(log_position):
    print('Hola')
    return 'p'

def staff_treasury(request):
    # VARIABLES GENERALES
    #comprueb si la sesión esta iniciada
    login = request.COOKIES.get('log_admin')
    Position = request.COOKIES.get('log_position')
    Name_admin = 'none'
    Position_admin1 = 'none'
    Position_admin2 = 'none'
    if Position == 'treasury' or Position == 'secretary' or Position == 'direction':

        objs = Admins.objects.filter(position=Position).values('name', 'fullname').first()
        Name_admin = objs['name']
        if Position == 'treasury':
            Position_admin1 = 'Tesorera'
            Position_admin2 = 'Tesoreria'
        elif Position == 'secretary':
            Position_admin1 = 'Secretaria'
            Position_admin2 = 'Secretaría'
        else:
            Position_admin1 = 'Director'
            Position_admin2 = 'Dirección'

    else:
        #Mostramos la pagina de login
        #No borraremos la cookie por que no pude hacerlo :3
        return render(request, 'ils_admin.html')

        


    objs = fut.objects.exclude(stage__exact=3).filter(route=Position).values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')

    if login == None:
        return render(request, 'ils_admin.html')
    
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
        
        #reason.append(i['reason'][:40])
    len_list_data = len(list_data)
    return render(request, 'admin/staff_treasury.html', {
        'Object': list_data,
        'Len_list_data': len_list_data,
        'views': num_no_view,
        'total_futs': total_futs,
        #admin data
        'Position1': Position_admin1,
        'Position2': Position_admin2,
        'Name': Name_admin
    })

def staff_secretary(request):
    objs = fut.objects.exclude(stage__exact=3).filter(route='treasury').values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')

    #comprueb si la sesión esta iniciada
    valor_cookie = request.COOKIES.get('log_admin')
    if valor_cookie == None:
        return render(request, 'ils_admin.html')
    
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
    for i in objs:
        diccionary={}
        diccionary['id'] = i['id']
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        diccionary['stage'] = i['stage']
        diccionary['view'] = i['view']
        list_data.append(diccionary)
        
        #reason.append(i['reason'][:40])
    len_list_data = len(list_data)
    return render(request, 'admin/staff.html', {
        'Object': list_data,
        'Len_list_data': len_list_data,
        'views': num_no_view,
        'total_futs': total_futs
    })

def view_fut(request):
    code_ = request.GET.get('code')
    # el 'mode' es para determinar que botones mostrar
    mode = request.GET.get('mode')

    Position = request.COOKIES.get('log_position')

    objs = fut.objects.filter(code=code_).values('id', 'myrequest', 'name', 'program', 'phone', 'dni', 'cycle', 'reason', 'email', 'order', 'date').first()

    # actualizamos el campo view
    up_register = fut.objects.get(code=code_)
    up_register.view = 1
    up_register.save()

    print("ENTRAMOS A VIEW FUT")

    return render(request, 'admin/staff/view_fut.html', {
        'code': code_,
        'objs': objs,
        'mode': mode,
        'position': Position
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
    Position = request.COOKIES.get('log_position')
    objs = fut.objects.filter(stage=1, route=Position).values('order', 'reason', 'name', 'dni', 'code')

    #names_short = [str(ob['order'])[:6] for ob in objs]
    
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        list_data.append(diccionary)
        
        #reason.append(i['reason'][:40])
    len_list_data = len(list_data)
    return render(request, 'admin/staff/postulated.html', {
        'Object': list_data,
        'Len_list_data': len_list_data
    })
def pending(request):
    objs = fut.objects.filter(stage=2).values('order', 'reason', 'name', 'dni', 'code')

    #names_short = [str(ob['order'])[:6] for ob in objs]
    
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        list_data.append(diccionary)
        
        #reason.append(i['reason'][:40])
    len_list_data = len(list_data)
    return render(request, 'admin/staff/pending.html', {
        'Object': list_data,
        'Len_list_data': len_list_data
    })

def send(request):
    Position = request.COOKIES.get('log_position')
    send_position = 'none'
    if Position == 'treasury':
        send_position = 'secretary'
    elif Position == 'secretary':
        send_position = 'direction'
    else:
        send_position = 'send_exit'

    objs = fut.objects.filter(route=send_position).values('order', 'reason', 'name', 'dni', 'code')

    #names_short = [str(ob['order'])[:6] for ob in objs]
    
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        diccionary['code'] = i['code']
        list_data.append(diccionary)
        #reason.append(i['reason'][:40])
    len_list_data = len(list_data)
    print('ESTAMOS EN SEND')
    return render(request, 'admin/staff/send.html', {
        'Object': list_data,
        'Len_list_data': len_list_data
    })

def name_admin(position):
    objs = Admins.objects.filter(position=position).values('name', 'fullname').first()
    name = objs['name']+' '+objs['fullname']
    return name

def save_process(tittle, name, reception, exit, state, num, fut_id, stage):
    my_objet = process(tittle = tittle, name = name, reception = reception, exit = exit, state = state, num = num, fut_id_id = fut_id, stage = stage)
    my_objet.save()
    new_id = my_objet.id
    return new_id

def send_01_treasurer(request):
    ticket = request.GET.get('ticket')
    id = request.GET.get('id')
    #obtenemos la cookie para realizar el proceso de envio
    Position = request.COOKIES.get('log_position')
    send_position = 'none'
    route_send = 'none'
    stage = 0
    num = 0

    print("HASTA AQUÍ TODO BIEN")
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

    #Insert in the BD
    admin_name = name_admin(Position)
    new_id = save_process(route_send, admin_name, date_format, None, False, num, id, stage)

    message = 'successful'
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