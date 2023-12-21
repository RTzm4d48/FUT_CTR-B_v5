from django.contrib import admin
from .models import Admins, process, document, secretary_send_document, direction_public_document, ticket, ticket_desarrollo
# Register your models here.


admin.site.register(Admins)
admin.site.register(process)
admin.site.register(document)

admin.site.register(secretary_send_document)
admin.site.register(direction_public_document)

admin.site.register(ticket)
admin.site.register(ticket_desarrollo)