from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import fut
# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')

def treasury(request):
    print('jelouda locoooo')
    objs = fut.objects.exclude(stage__exact=3).values('order', 'reason', 'name', 'dni', 'code')

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
    return render(request, 'admin/staff.html', {
        'Object': list_data,
        'Len_list_data': len_list_data
    })

def view_fut(request):
    code_ = request.GET.get('code')
    objs = fut.objects.filter(code=code_).values('id', 'myrequest', 'name', 'program', 'phone', 'dni', 'cycle', 'reason', 'email', 'order', 'date').first()

    return render(request, 'admin/staff/view_fut.html', {
        'code': code_,
        'objs': objs
    })

def view_send(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        stage_ = request.GET.get('stage')

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