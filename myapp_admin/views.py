from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
from myapp_admin.models import process

#para saber el dia y la hora actual
from datetime import datetime
from datetime import date

# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')

def staff(request):
    objs = fut.objects.exclude(stage__exact=3).values('id', 'order', 'reason', 'name', 'dni', 'code', 'stage', 'view')

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
    objs = fut.objects.filter(code=code_).values('id', 'myrequest', 'name', 'program', 'phone', 'dni', 'cycle', 'reason', 'email', 'order', 'date').first()

    # actualizamos el campo view
    up_register = fut.objects.get(code=code_)
    up_register.view = 1
    up_register.save()

    return render(request, 'admin/staff/view_fut.html', {
        'code': code_,
        'objs': objs
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
    objs = fut.objects.filter(stage=1).values('order', 'reason', 'name', 'dni', 'code')

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
    objs = fut.objects.filter(stage=3).values('order', 'reason', 'name', 'dni', 'code')

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
    return render(request, 'admin/staff/send.html', {
        'Object': list_data,
        'Len_list_data': len_list_data
    })

def save_process(tittle, name, reception, exit, state, num, fut_id, stage):
    my_objet = process(tittle = tittle, name = name, reception = reception, exit = exit, state = state, num = num, fut_id_id = fut_id, stage = stage)
    my_objet.save()
    new_id = my_objet.id
    return new_id

def send_01_treasurer(request):
    ticket = request.GET.get('ticket')
    id = request.GET.get('id')

    print(ticket)
    print(id)

    #actualizamos los datos de 'FUT'
    up_register = fut.objects.get(id=id)
    up_register.n_ticket = ticket
    up_register.route = 'secretary'
    up_register.stage = 0
    up_register.view = 0
    up_register.save()

    #obtener the date
    date = datetime.now() 
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")

    #Actualizamos los datos de 'admin_process'
    up_process_2 = process.objects.get(stage=1)
    up_process_2.exit = date_format

    #Insert in the BD
    new_id = save_process('SECRETARIA', 'Jessica Rodríguez Sanchez', date_format, None, False, 60, id, 2)

    message = 'successful'
    return JsonResponse({'message': message})