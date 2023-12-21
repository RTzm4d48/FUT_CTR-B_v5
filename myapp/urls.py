from django.urls import path, include
from . import views # corto y pego de ./mysite/urls.py
from . import vws_createfut_process
from . import views_createFUT
from . import views_notification
from . import views_view_fut
from . import views_observations

urlpatterns = [
    path('', views.index, name="n_home"), # corto y pego de ./mysite/urls.py
    
    path('my_fut', views.my_fut),
    
    # views.py AQUI ESTAN TODAS LA DIRECCIONES PARA CREAR EL FUT
    path('form_new_fut/identification', views.form_new_fut, name="n_new_fut"),
    path('form_new_fut/processtd', views.create_fut_process, name="n_process"),
    path('form_new_fut/pay', views.create_fut_pay, name="n_pay"),
    path('form_new_fut/finisher/', views_createFUT.finisher, name="n_end"),
    path('form_new_fut/successful', views.successful, name="n_successful"),
    path('async-data/', views.async_data, name="n_test"),

    # vws_createfut_process AQUI GESTIONAMOS TODO SOBRE LA CREACION DEL FUT
    path('my_fut/proceedings', vws_createfut_process.proceedings, name="n_proceedings"),
    path('my_fut/download_image', vws_createfut_process.download_image, name="n_img_dow"),
    path('my_fut/my_credentials_EMAIL', vws_createfut_process.my_credentials_email, name="n_send_email"),
    path('send_email/', vws_createfut_process.send_email, name='n_send_email'),
    path('procedures_list/', vws_createfut_process.procedures_list, name='n_procedures_list'),
    path('tupa_validation_path/', vws_createfut_process.tupa_validation, name="n_tupa_validation"),
    # login
    path('logout/', views.exit, name='n_exit'),

    # view fut
    #vws_view_fut AQUI ESTARA TODAS LAS VITAS PARA VER EL TRAMITE REALIZADO
    path('my_fut/fut_consult_path/', views_view_fut.fut_consult, name="n_fut_consult"),
    path('my_fut/fut_all_path', views_view_fut.fut_all, name="n_fut_all"),
    path('my_fut/fut_process_path', views_view_fut.fut_process, name="n_fut_process"),
    path('my_fut/fut_finish_path', views_view_fut.fut_finish, name="n_fut_finish"),

    
    path('loader', views.view_loader, name='n_loader'),

    # NOTIFICACIONES
    path('get_message_ticket_path/', views_notification.get_message_ticket, name="n_get_message_ticket"),
    path('get_notification_path/', views_notification.get_notification, name="n_get_notification"),
    path('open_fut_path/', views_notification.open_fut, name="n_open_fut"),

    # VIEWS OF VIEW FUT
    path('tracking_path/', views_view_fut.tracking, name="n_tracking"),
    path('pros_route_path/', views_view_fut.pros_route, name="n_pros_route"),
    path('view_fut_path/', views_view_fut.view_fut, name="n_view_fut"),

    # OBSERVACIONES
    path('my_fut/observation/', views_observations.init_observations, name="n_init_observations"),
    path('my_fut/observation/tickets', views_observations.tickets_path, name="n_tickets_path"),
    path('my_fut/observation/Reportes', views_observations.report_path, name="n_report_path"),
    path('my_fut/observation/show', views_observations.show_path, name="n_show_path"),
    path('my_fut/observation/show_redirect/<str:code>/', views_observations.redirect_show, name="n_redirect_show"),
    # funciones
    path('get_db_ticket_path/', views_observations.get_db_ticket, name="n_get_db_ticket"),
    path('get_desarrollo_db_path/', views_observations.get_desarrollo_db, name="n_get_desarrollo_db"),
    path('update_desarrollo_ticket_path/', views_observations.update_desarrollo_ticket, name="n_update_desarrollo_ticket"),
    path('create_user_ticket_path/', views_observations.create_user_ticket, name="n_create_user_ticket"),

]