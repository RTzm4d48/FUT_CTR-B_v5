from django.urls import path, include
from . import views # corto y pego de ./mysite/urls.py

urlpatterns = [
    path('', views.index, name="n_home"), # corto y pego de ./mysite/urls.py
    path('form_new_fut/identification', views.form_new_fut, name="n_new_fut"), #corto y pego de ./mysite/urls.py
    path('my_fut', views.my_fut),
    
    path('form_new_fut/processtd', views.create_fut_process, name="n_process"),
    path('form_new_fut/pay', views.create_fut_pay, name="n_pay"),
    path('form_new_fut/wait_payment', view.create_fut_wait, name="n_wait"),
    path('form_new_fut/finisher', views.finisher, name="n_end"),
    path('form_new_fut/successful', views.successful, name="n_successful"),

    path('my_fut/proceedings', views.proceedings, name="n_proceedings"),

    path('my_fut/download_image', views.download_image, name="n_img_dow"),
    path('my_fut/my_credentials_EMAIL', views.my_credentials_email, name="n_send_email"),

    path('send_email/', views.send_email, name='n_send_email'),
    path('procedures_list/', views.procedures_list, name='n_procedures_list'),
    # login
    path('logout/', views.exit, name='n_exit'),

    # view fut
    path('my_fut/in-progress', views.view_fut_in_progress, name='n_in_progress'),
    path('my_fut/finished', views.view_fut_finished, name='n_finished'),

]