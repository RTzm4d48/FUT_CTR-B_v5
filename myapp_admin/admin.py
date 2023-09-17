from django.contrib import admin
from .models import Admins, process, document
# Register your models here.


admin.site.register(Admins)
admin.site.register(process)
admin.site.register(document)