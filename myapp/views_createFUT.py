from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#from django.views import View
import asyncio
from asgiref.sync import async_to_sync
from datetime import date, datetime

# IMPORTAR VISTAS
from myapp.views_createFUT_process import generate_proceedings
from myapp.views_createFUT_process import generate_code
from myapp.views_createFUT_process import generate_qrcode
from myapp.views_createFUT_process import generate_email
from myapp.views_createFUT_process import save_my_objet
from myapp.views_createFUT_process import get_monto
from myapp.views_createFUT_process import guardar_archivo_enTmp
from myapp.views_createFUT_process import obtener_archivo_deTmp
from myapp.views_createFUT_process import save_process
from myapp.views_createFUT_process import name_admin
from myapp.views_createFUT_process import insert_notification

import base64

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
        attach_file_name = request.POST.get('attach_file_name')
        # PAY
        type_pay = request.POST.get('typepay')
        id_user = request.POST.get('user')
        # img de pago
        if 'img_pay' in request.FILES:
            img_file = request.FILES['img_pay']
            pay_img_binary = img_file.read()
            pay_img_binary_encoded = base64.b64encode(pay_img_binary)
        else:
            pay_img_binary_encoded = b''# bynary bacio

        # OBTENDREMOS EL ARCHIVO attach EN byte DE tmp
        attach_byte = await obtener_archivo_deTmp(attach_file_name);
        
        #obtener the date
        date_ = datetime.now()# output: 2023-11-21 15:24:10.832093
        date_format = date_.strftime("%Y-%m-%d %H:%M:%S")
      
        now_date = date.today()# output: 2023-11-21

        exp_, pas_ = await generate_proceedings()
        monto = await get_monto(order_id)
        code_ = await generate_code()
        print('STEP_01')
        qrimg_bytes = await generate_qrcode(code_)
        print('STEP_02')
        # await generate_email(email, name, exp_, pas_)
        print('STEP_03')
        new_id = await save_my_objet(name, full_name, program, dni, phone, cycle, email, myrequest, order, reason, now_date, attach_byte, exp_, pas_, code_, qrimg_bytes, monto, 1, pay_img_binary_encoded, type_pay, id_user) #2 is treasury id
        print('STEP_04')
        # INSERTAMOS UNA ruta_tramite
        await save_process('TRAMITE EN CURSO', 'INSTITUTO LATINOAMERICANO SIGLO XXI', date_format, date_format, new_id)
        print('STEP_05')
        # obtenemos el nombrede la tesoreria para introducirlo en el modelo ruta_tramite
        admin_name = await name_admin('treasury')
        await save_process('TESORERIA', admin_name, date_format, None, new_id)
        print('STEP_06')
        await insert_notification(new_id, id_user, date_format)
   
        return render(request, 'create_fut/form_post_create_fut.html', {
            'Fut_id': new_id
        })
        
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    