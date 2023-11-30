from django.urls import path
from . import views
from . import views_process
from . import views_tickets
from . import views_report
from . import views_FUTprocess

urlpatterns = [
    path('ils_admin', views.ilsadmin, name="n_ilsadmin"),
    path('ils_admin/staff_treasury', views.staff_treasury,name="n_staff_treasury"),
    path('ils_admin/staff/fut', views.view_fut, name="n_view_fut"),
    path('viewsend/', views.view_send, name='view_send'),
    path('ils_admin/staff/fut_postulated', views.postulated, name="n_postulated"),
    path('ils_admin/staff/fut_pending', views.pending, name="n_pending"),
    path('ils_admin/staff/fut_send', views.send, name="n_send"),
    path('ils_admin/staff/reported', views.reported, name="n_reported"),
    path('send_01/', views.send_01_treasurer, name="n_send_01"),
    path('admin_login/', views.admin_login, name="n_admin_login"),
    path('send_inssued/', views.send_inssued, name="n_send_inssued"),
    path('send_document/', views_process.send_document, name="n_send_document"),

    path('ils_admin/staff_treasury2', views.next, name="n_next"),

    path('download/', views_process.direction_download, name="n_download"),

    # views_ticket AQUI ESTAN TODAS LAS URLS PARA views_ticket.py
    path('create_ticket_path/', views_tickets.create_ticket, name="n_create_ticket"),
    path('update_desarrollo_path/', views_tickets.update_desarrollo, name="n_update_desarrollo"),
    path('loading_ticket_path/', views_tickets.loading_ticket, name="n_loading_ticket"),
    path('more_loading_ticket_path/', views_tickets.moreloading_ticket, name="n_more_loading_ticket"),


    # views_report AQUI ESTAN TODAS LAS URLS PARA LAS VISTAS DE views_report.py
    path('create_report_path/', views_report.create_report, name="n_create_report"),
    path('select_report_path/', views_report.select_report, name="n_select_report"),

    # AQUI ESTARAN TODAS LAS VISTAS PARA PROCESAR LOS FUTS
    path('process_fut_path/', views_FUTprocess.process_fut, name="n_process_fut"),
]