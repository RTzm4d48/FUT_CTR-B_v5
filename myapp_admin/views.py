from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ilsadmin(request):
    return render(request, 'ils_admin.html')

def treasury(request):
    return render(request, 'admin/treasury.html')