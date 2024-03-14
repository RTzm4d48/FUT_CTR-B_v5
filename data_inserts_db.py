# python manage.py shell *POR SI HACE FALTA HACERLO EN CONSOLA

from myapp.models import tupa

# TODOS LOS DATOS A INSRTAR EN TUPA
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Cambio de Programa", monto=25, duracion_de_tramite=5, procedimiento="Trámite que lleva un proceso, para la convalidación de programa, con RD.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Cambio de Turno", monto=20, duracion_de_tramite=5, procedimiento="Tramite de traslado interno de turno y horario, con RD.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Bienestar", tipo_de_servicio="Carta de Presentación practica Pre-Prof", monto=20, duracion_de_tramite=7, procedimiento="Carta de presentación para practicas pre profesionales, Adjuntar copia de convenio.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado de estudios (Pagar por cada ciclo)", monto=90, duracion_de_tramite=7, procedimiento="Documento que certifica los promedios por ciclo, (S/. 15 por cada ciclo S/.90).")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado modular por año", monto=35, duracion_de_tramite=7, procedimiento="Certificado que valida la culminación satisfactoría del año.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado de Formación Continua", monto=35, duracion_de_tramite=7, procedimiento="Certificado que valida la culminación del curso.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado Progresivo", monto=30, duracion_de_tramite=7, procedimiento="Certificado que valida la culminación satisfactoría del ciclo.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Egresado", monto=20, duracion_de_tramite=7, procedimiento="Documento que certifica el termino del programa.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Estudios", monto=15, duracion_de_tramite=7, procedimiento="Documento que certifica que una persona cursa un programa de estudios.")
tupa_data.save()
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Otros", monto=0, duracion_de_tramite=7, procedimiento="Procedimiento Indefinido.")
tupa_data.save()


# INSER TO ADMINS

from myapp_admin.models import Admins

admin_data = Admins(name="Diana Marta", fullname="Pachecco Miraflores", email="useradmin@ils.edu.pe", position="treasury", phone="987365467", dni="7637465", password="password")
admin_data.save()
admin_data = Admins(name="Ana Faviola", fullname="Aguirre Mamani", email="useradmin@ils.edu.pe", position="secretary", phone="987365467", dni="7637465", password="password")
admin_data.save()
admin_data = Admins(name="Luis Roman", fullname="Aguirre Sanchez", email="useradmin@ils.edu.pe", position="direction", phone="987365467", dni="7637465", password="password")
admin_data.save()
