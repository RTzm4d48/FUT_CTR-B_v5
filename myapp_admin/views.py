from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import fut
# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')

def treasury(request):
    print('jelouda locoooo')
    objs = fut.objects.filter(stage=0).values('order', 'reason', 'name', 'dni')

    #names_short = [str(ob['order'])[:6] for ob in objs]
    
    #modifico el numero de caracteres del los datos de los diccionarios y los agrego a la lista 'list_data'
    list_data = []
    for i in objs:
        diccionary={}
        diccionary['order'] = i['order'][:30]
        diccionary['reason'] = i['reason'][:40]
        diccionary['name'] = i['name'][:50]
        list_data.append(diccionary)
        
        #reason.append(i['reason'][:40])

    print('-------------------------------------------')
    print(list_data)
    return render(request, 'admin/treasury.html', {
        'Object': list_data
    })