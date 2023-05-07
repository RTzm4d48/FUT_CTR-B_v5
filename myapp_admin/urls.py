from django.urls import path
from . import views

urlpatterns = [
    path('ils_admin', views.ilsadmin, name="n_ilsadmin"),
    path('ils_admin/treasury', views.treasury,name="n_treasury"),
]