import json
from asgiref.sync import sync_to_async, async_to_sync
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import fut, tupa
from myapp_admin.models import process, Admins

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

#Para el login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




from django.urls import reverse

# para descargar una imagen
from django.conf import settings
import os



#para saber el dia y la hora actual




def index(request):
    return render(request,'index.html')

@login_required
@csrf_exempt
def my_fut(request):
    my_list_ = list(range(10))
    my_list = [i + 5 for i in range(10)]
    var = 5
    return render(request, 'view_fut/fut.html', {
        'some_list': my_list,
        'var': var
    })

def exit(request):
    logout(request)
    return redirect('n_home')

@login_required
def mylogin(request):
    return redirect('n_home')

@login_required
def form_new_fut(request):
    return render(request, 'create_fut/identification.html')


def create_fut_process(request):
    if request.method=='POST':
        name = request.POST.get('name')
        full_name = request.POST.get('full_name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')

        return render(request, 'create_fut/process.html', {
            'Name': name,
            'Full_name': full_name,
            'Email': email,
            'Phone': phone,
            'Dni': dni,
            'Cycle': cycle,
            'Program': program
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    
def get_monto(order_id):
    obj = tupa.objects.filter(id=order_id).values('monto').first()
    monto = obj['monto']
    return monto

from django.core.files.storage import FileSystemStorage
def guardar_archivo_enTmp(pdf_file):
    #GUARDAREMOS EL PDF
    print("ESTAMOH GUARDANDO LO")
    # static_path = 'myapp/static/tmp/'
    static_path = os.path.join(settings.STATIC_ROOT, 'tmp')

    fs = FileSystemStorage(location=static_path)
    fs.save(pdf_file.name, pdf_file)
    print(pdf_file.name)
    return pdf_file.name

@csrf_exempt
def create_fut_pay(request):
    if request.method=='POST':
        # identification
        name = request.POST.get('name')
        full_name = request.POST.get('full_name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        order_id = request.POST.get('order_id')
        reason = request.POST.get('reason')

        monto = get_monto(order_id)

        # my es solicito
        if(myrequest == ""):myrequest="null"
        
        # Procedimiento con el PDF
        # Validando si se envio el pdf
        if 'attach_file' in request.FILES:
            attach_file = request.FILES['attach_file']
            #pdf_binary = attach_file.read()
            #pdf_binary_encoded = base64.b64encode(pdf_binary)

            #GUARDAREMOS EN tmp
            attach_file_name = guardar_archivo_enTmp(attach_file)
        else:
            attach_file_name = "false"

        return render(request, 'create_fut/pay.html', {
            'yape_num': settings.YAPE_NUM,
            'yape_name': settings.YAPE_NAME,
            'Name': name,
            'Full_name': full_name,
            'Email': email,
            'Phone': phone,
            'Dni': dni,
            'Cycle': cycle,
            'Program': program,
            'Myrequest': myrequest,
            'Order': order,
            'Order_id': order_id,
            'Monto': monto,
            'Reason': reason,
            'Attach_file_name': attach_file_name
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
async def finisher(request):
    if request.method == 'POST':
        # identification
        name = request.POST.get('name')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dni = request.POST.get('dni')
        cycle = request.POST.get('cycle')
        program = request.POST.get('program')
        # TRAMITE
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        order_id = request.POST.get('order_id')
        reason = request.POST.get('reason')

        print("AQUI_BIEN")

        now_date = date.today()
        
        
        

        # exp_, pas_ = await generate_proceedings()

        # code_ = await generate_code()
        # print('LOCURA_01')
        # qrimg_bytes = await generate_qrcode(code_)
        # print('LOCURA_02')
        # # nnn = await generate_email(email, name, exp_, pas_)
        # print('LOCURA_03')
        # new_id = await save_my_objet(name, program, dni, phone, cycle, email, myrequest, order, reason, now_date, exp_, pas_, code_, qrimg_bytes)
        # print('LOCURA_04')
        # # CRUD en el modelo 'Process'
        # #obtener the date
        # date_ = datetime.now() 
        # date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
        # print('LOCURA_05')
        # await save_process('TRAMITE EN CURSO', 'INSTITUTO LATINOAMERICANO SIGLO XXI', date_format, date_format, False, 20, new_id, 0)
        # print('LOCURA_06')
        # # obtenemos el nombrede la tesoreria para introducirlo en el modelo process
        # admin_name = await name_admin('treasury')
        # await save_process('TESORERIA', admin_name, date_format, None, False, 40, new_id, 1)

        Names = "Recardo"
        return render(request, 'create_fut/successful.html',{
            'Name': Names
        })
    
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    
    
def successful(request):
    if request.method == 'POST':
        my_id = request.POST.get('id_value')

        obj = fut.objects.filter(id=my_id).values('name', 'full_name', 'dni', 'order', 'proceeding', 'password', 'code').first()

        resultados_json = list(obj)

        print('SUEÑOS')
        print(resultados_json)
        print(obj)

        return render(request, 'create_fut/successful.html', {
            'data': obj
        })
    else:
        return HttpResponse("<h1>404 ESTA URL NO EXISTE :(</h1>")

def create_fut_wait(request):
    if request.method == 'POST':
         # identification
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        email = request.POST.get('email')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')
        pdf_memoryview = request.POST.get('pdf_binary_encoded')
        
        if pdf_memoryview == 'null':
            pdf_bytes = bytes()
        else:
            pdf_bytes = pdf_memoryview.encode("utf-8")

        now_date = date.today()
        return render(request, 'create_fut/create_fut_wait.html',{
            'Name': name,
            'Program': program,
            'Dni': dni,
            'Phone': phone,
            'Cycle': cycle,
            'Email': email,
            'Myrequest': myrequest,
            'Order': order,
            # 'Order_id': order_id,
            # 'Monto': monto,
            'Reason': reason,
            # 'Pdf_binary_encoded': pdf_binary_encoded
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")

def pueba_vw():
    return "PATATO"

def view_loader(request):
    return render(request,'loader.html')

#CREAMOS UNA VISTA DE PRUEBA PARA LA FINALIZACION DE CREATE FUT
from django.http import JsonResponse

def async_data(request):

    if request.method == 'GET':
         # identification
        name = request.GET.get('name')
        program = request.GET.get('program')
        dni = request.GET.get('dni')
        phone = request.GET.get('phone')
        cycle = request.GET.get('cycle')
        email = request.GET.get('email')
        # process
        myrequest = request.GET.get('myrequest')
        order = request.GET.get('order')
        reason = request.GET.get('reason')
        #pdf_memoryview = request.POST.get('pdf_binary_encoded')
        
        #if pdf_memoryview == 'null':
         #   pdf_bytes = bytes()
        #else:
         #   pdf_bytes = pdf_memoryview.encode("utf-8")


        print(name);
        print(program);
        print(dni);
        print(phone);
        print(cycle);
        print(email);
        print(myrequest);
        print(order);
        print(reason);
    # Simula la carga de datos (reemplaza esto con tu lógica de carga de datos)
    import time
    time.sleep(3)

    data = {
        'message': 'Datos cargados exitosamente',
        'content': 'Contenido de tus datos aquí',
    }

    return JsonResponse(data)