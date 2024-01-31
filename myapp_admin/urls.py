from django.urls import path
from . import views_get_fut
from . import views_process
from . import views_tickets
from . import views_report
from . import views_FUTprocess
from . import views_get_fut

urlpatterns = [
    path('ils_admin', views_get_fut.ilsadmin, name="n_ilsadmin"),
    path('ils_admin/staff_treasury', views_get_fut.staff_treasury,name="n_staff_treasury"),
    path('ils_admin/staff/fut', views_get_fut.view_fut, name="n_view_fut"),
    path('obtain_img/', views_get_fut.obtain_img, name="n_obtain_img"),
    path('viewsend/', views_get_fut.view_send, name='view_send'),
    path('ils_admin/staff/fut_postulated', views_get_fut.postulated, name="n_postulated"),
    path('ils_admin/staff/fut_pending', views_get_fut.pending, name="n_pending"),
    path('ils_admin/staff/fut_send', views_get_fut.send, name="n_send"),
    path('ils_admin/staff/reported', views_get_fut.reported, name="n_reported"),
    path('send_01/', views_get_fut.send_01_treasurer, name="n_send_01"),
    path('admin_login/', views_get_fut.admin_login, name="n_admin_login"),
    path('send_inssued/', views_get_fut.send_inssued, name="n_send_inssued"),
    path('send_document/', views_process.send_document, name="n_send_document"),

    path('ils_admin/staff_treasury2', views_get_fut.next, name="n_next"),

    path('download/', views_process.direction_download, name="n_download"),

    # views_ticket AQUI ESTAN TODAS LAS URLS PARA views_ticket.py
    path('create_ticket_path/', views_tickets.create_ticket, name="n_create_ticket"),
    path('update_desarrollo_path/', views_tickets.update_desarrollo, name="n_update_desarrollo"),
    path('pueba_path/', views_tickets.prueba, name="n_prueba"),
    path('observation_reply_path/', views_tickets.observation_reply, name="n_observation_reply"),
    path('loading_ticket_path/', views_tickets.loading_ticket, name="n_loading_ticket"),
    path('more_loading_ticket_path/', views_tickets.moreloading_ticket, name="n_more_loading_ticket"),
    path('all_desarrollo_data_path/', views_tickets.all_desarrollo_data, name="n_all_desarrollo_data"),

    # views_report AQUI ESTAN TODAS LAS URLS PARA LAS VISTAS DE views_report.py
    path('create_report_path/', views_report.create_report, name="n_create_report"),
    path('select_report_path/', views_report.select_report, name="n_select_report"),

    # AQUI ESTARAN TODAS LAS VISTAS PARA PROCESAR LOS FUTS
    path('process_fut_path/', views_FUTprocess.process_fut, name="n_process_fut"),
    path('write_myFile_path/', views_FUTprocess.write_myFile, name="n_write_myFile"),# ESTO HAY QUE BORRAR
    path('secretary_process_doc_path/', views_FUTprocess.secretary_process_doc, name="n_secretary_process_doc"),
    path('direction_process_doc_path/', views_FUTprocess.direction_process_doc, name="n_direction_process_doc"),
    path('download_doc_path/', views_FUTprocess.download_doc, name="n_download_doc"),
    path('direct_download_path/', views_FUTprocess.direct_download, name="n_direct_download"),
]