from django.urls import path
from . import views

urlpatterns = [
    path('ils_admin', views.ilsadmin, name="n_ilsadmin"),
]