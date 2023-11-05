from django.urls import path, include
from . import views # corto y pego de ./mysite/urls.py
from . import vws_createfut_process
from . import vws_view_fut

urlpatterns = [
    path('', views.index, name="n_home"), # corto y pego de ./mysite/urls.py
    
    path('my_fut', views.my_fut),
    
    # views.py AQUI ESTAN TODAS LA DIRECCIONES PARA CREAR EL FUT
    path('form_new_fut/identification', views.form_new_fut, name="n_new_fut"),
    path('form_new_fut/processtd', views.create_fut_process, name="n_process"),
    path('form_new_fut/pay', views.create_fut_pay, name="n_pay"),
    path('form_new_fut/finisher', views.finisher, name="n_end"),
    path('form_new_fut/successful', views.successful, name="n_successful"),

    # vws_createfut_process AQUI GESTIONAMOS TODO SOBRE LA CREACION DEL FUT
    path('my_fut/proceedings', vws_createfut_process.proceedings, name="n_proceedings"),
    path('my_fut/download_image', vws_createfut_process.download_image, name="n_img_dow"),
    path('my_fut/my_credentials_EMAIL', vws_createfut_process.my_credentials_email, name="n_send_email"),
    path('send_email/', vws_createfut_process.send_email, name='n_send_email'),
    path('procedures_list/', vws_createfut_process.procedures_list, name='n_procedures_list'),

    # login
    path('logout/', views.exit, name='n_exit'),

    # view fut
    #vws_view_fut AQUI ESTARA TODAS LAS VITAS PARA VER EL TRAMITE REALIZADO
    path('my_fut/in-progress', vws_view_fut.view_fut_in_progress, name='n_in_progress'),
    path('my_fut/finished', vws_view_fut.view_fut_finished, name='n_finished'),

]