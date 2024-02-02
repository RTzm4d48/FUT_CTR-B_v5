# python manage.py shell *POR SI HACE FALTA HACERLO EN CONSOLA
from myapp.models import tupa

#1
# TODOS LOS DATOS A INSRTAR EN TUPA
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Búsqueda de documentos", monto=25, duracion_de_tramite=7, procedimiento="Búsqueda de docúmentos tramitados anteriormente.")
tupa_data.save()

#2
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Cambio Interno de Carrera Profesional", monto=35, duracion_de_tramite=5, procedimiento="Proceso para la Convalidacion de la Carrera.")
tupa_data.save()

#3
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Cambio de Turno", monto=30, duracion_de_tramite=5, procedimiento="Traslado Interno de Turno u Horario.")
tupa_data.save()

#4
tupa_data = tupa(areas_incolucradas="Bienestar", tipo_de_servicio="Carta Presentacion Practicas-Pre-Profesionales de Carrera", monto=30, duracion_de_tramite=7, procedimiento="Carta de Presentacion Para Practicas-Pre-Profesionales. Adjuntar Copia de Convenio.")
tupa_data.save()

#5
tupa_data = tupa(areas_incolucradas="Tesoreria", tipo_de_servicio="Ceremonia Protocolar", monto=125, duracion_de_tramite=15, procedimiento="Ceremonia Para Entrega del Diploma de Egresado o Titulo Profesional.")
tupa_data.save()

#6
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado de Buena Conducta", monto=30, duracion_de_tramite=7, procedimiento="Certificado que Acredita la Buena Conducta del Alumno.")
tupa_data.save()

#7
#esto mira
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado de Estudios de Carrera Profesional", monto=125, duracion_de_tramite=7, procedimiento="Documento que Certifica los Promedios Por Ciclo y Cursos que llevo el Alumn@")
tupa_data.save()

#8
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado Modular por Año de Carrera Profesional", monto=45, duracion_de_tramite=7, procedimiento="Certificado que Valida la Culminacion Satisfactoria por Año")
tupa_data.save()

#9
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado de Formacion Continua (Ingles,Office,Cajero,Etc,Adm Bancaria)", monto=45, duracion_de_tramite=7, procedimiento="Certificado que Valida la Culminacion del Curso")
tupa_data.save()

#10
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Certificado Progresivo de Carrera Profesional", monto=40, duracion_de_tramite=7, procedimiento="Certificado que Valida la Culminacion Satisfactoria del Ciclo o Semestre")
tupa_data.save()

#11
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Egresado de Carrera Profesional", monto=30, duracion_de_tramite=7, procedimiento="Documento que Certifica el Termino de la Carrera")
tupa_data.save()

#12
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Estudios de Carrera Profesional o de Formacion Continua", monto=25, duracion_de_tramite=7, procedimiento="Documento que Certifica el Ciclo y Carrera que Cursa el Alumn@")
tupa_data.save()

#13
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Matricula Carrera y Formacion Continua", monto=30, duracion_de_tramite=7, procedimiento="Documento que Hace Constar la Matricula de un Alumn@")
tupa_data.save()


#14
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Notas Carreras y Formacion Continua", monto=30, duracion_de_tramite=7, procedimiento="Documento que Certifica los Promedios por Ciclo y Cursos que llevo")
tupa_data.save()


#15
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de No Adeudar", monto=30, duracion_de_tramite=7, procedimiento="Documento que Certifica que un Alumno no Tiene Deuda con la Institucion")
tupa_data.save()


#16
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Titulo en Tramite", monto=30, duracion_de_tramite=7, procedimiento="Documento que Consta que el Alumn@ esta Tramitando del Titulo")
tupa_data.save()

#17
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Constancia de Vacante de Carrera Profesional", monto=30, duracion_de_tramite=7, procedimiento="Documento que Certifica que Existe Vacante Para Translado Externo")
tupa_data.save()

#Ver esto
#18
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Administracion de Empresas Modalidad Presencial", monto=280, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad de Programa")
tupa_data.save()

#Ver esto
#19
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Administracion de Empresas Modalidad Virtual", monto=170, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad del Programa")
tupa_data.save()

#Ver esto
#20
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Computacion e Informatica Modalidad Presencial", monto=280, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad del Programa")
tupa_data.save()

#Ver esto
#21
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Computacion e Informatica Modalidad Virtual", monto=170, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad del Programa")
tupa_data.save()

#Ver esto
#22
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Contabilidad Modalidad Presencial", monto=280, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad del Programa")
tupa_data.save()

#Ver esto
#23
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Cuota Mensual-Programa Contabilidad Modalidad Virtual", monto=170, duracion_de_tramite=5, procedimiento="Pago de la Mensualidad del Programa")
tupa_data.save()


#ver esto
#24
tupa_data = tupa(areas_incolucradas="Direccion de Gestion Academica/Secretaria Academica", tipo_de_servicio="Curso a Cargo de la Carrera Profesional", monto=85, duracion_de_tramite=90, procedimiento="Recuperacion de un Curso Desaprobado(Pago por cada mes)")
tupa_data.save()


#ver esto
#25
tupa_data = tupa(areas_incolucradas="Marketing/Caja", tipo_de_servicio="Curso a Cargo de Formacion Continua", monto=40, duracion_de_tramite=5, procedimiento="Recuperacion de un Curso Desaprobado(Pago por cada mes proporcional a la pension)")
tupa_data.save()

#ver esto
#26
tupa_data = tupa(areas_incolucradas="Direccion de Gestion Academica/Secretaria Académica ", tipo_de_servicio="Curso a Cargo del Programa de Titulacion Profesional", monto=375, duracion_de_tramite=1, procedimiento="Recuperacion de un Curso Desaprobado del Programa de Titulacion")
tupa_data.save()

#ver esto
#27
tupa_data = tupa(areas_incolucradas="Direccion de Gestion Financiero/Caja", tipo_de_servicio="Devolucion de Dinero", monto=30%, duracion_de_tramite=7, procedimiento="Se Hace la Devolucion Solo del Pago de Armada")
tupa_data.save()

#ver esto
#28
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Devolucion de Documentos", monto=0, duracion_de_tramite=7, procedimiento="Solo a Alumnos de I Ciclo Que Ya no Estudiaran")
tupa_data.save()


#29
tupa_data = tupa(areas_incolucradas="Direccion de Gestion Academica", tipo_de_servicio="Duplicado Carnet Estudiante ILS", monto=30, duracion_de_tramite=5, procedimiento="Copia Fiel del Original")
tupa_data.save()

#ver esto
#30
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Duplicado de Cert Modular-Duplicado de Cert Progresivo", monto=40.35, duracion_de_tramite=7, procedimiento="Copia Fiel del Original")
tupa_data.save()

#31
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Duplicado de Certificado(Taller,Charlas,Forum o Capacitaciones)", monto=20, duracion_de_tramite=7, procedimiento="Copia Fiel del Original")
tupa_data.save()


#32
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Duplicado de Diploma de Egresado", monto=80, duracion_de_tramite=7, procedimiento="Copia Fiel del Original")
tupa_data.save()

#ver esto
#33
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Duplicado de Titulo Profesional", monto=175, duracion_de_tramite=5, procedimiento="Copia Fiel del Original")
tupa_data.save()

#34
tupa_data = tupa(areas_incolucradas="Atencion al Alumno/Secretaria Académica", tipo_de_servicio="Examen de Cargo de Carrera Profesional", monto=165, duracion_de_tramite=5, procedimiento="Examen Para Alumnos que Tienen un Curso Desaprobado y que no se Encuentra en la Nueva Curricula o de Ultimo Ciclo que Adeuden un Curso")
tupa_data.save()


#35
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Examen Extemporaneo", monto=50, duracion_de_tramite=5, procedimiento="Examen Fuera de la Fecha Programada por el Docente")
tupa_data.save()

#36
tupa_data = tupa(areas_incolucradas="Atencion al Alumno", tipo_de_servicio="Examen Sustitutorio", monto=40, duracion_de_tramite=5, procedimiento="Examen que Sustituye la Nota Desaprobada de Recuperacion")
tupa_data.save()

#37
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Fedateo o Visado de Documentos por Hoja", monto=3.00, duracion_de_tramite=7, procedimiento="Dar Fe que el Documento que se Emitio en ILS es Copia Fiel")
tupa_data.save()

#38
tupa_data = tupa(areas_incolucradas="Bienestar Estudiantil", tipo_de_servicio="File de Practicas-Experiencias Formativas", monto=30, duracion_de_tramite=3, procedimiento="File de Experiencias Formativas para Alumnos Adjuntar Copia del Convenio")
tupa_data.save()

#ver esto
#39
tupa_data = tupa(areas_incolucradas="Caja", tipo_de_servicio="Formato Unico de Tramite", monto=3, duracion_de_tramite=1, procedimiento="Formato para Solicitar Tramites")
tupa_data.save()

#40
tupa_data = tupa(areas_incolucradas="Atencion al Alumno", tipo_de_servicio="Justificacion de Inasistencias", monto=30, duracion_de_tramite=5, procedimiento="Justificacion de Inasistencia por Motivos de Salud,Trabajo,Muerte de Algun Familiar en 1ER Grado o Viaje")
tupa_data.save()

#41
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Malla Curricular", monto=20, duracion_de_tramite=7, procedimiento="Unidades Didacticas Detalladas del Programa")
tupa_data.save()

#ver esto
#42
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Modificacion del Nombre en Titutlo Profesional por el Alumno", monto=100, duracion_de_tramite=, procedimiento="Cambio en el Nombre,Cuando el Alumno Ha Realizado su Tramite en Reniec")
tupa_data.save()


#43
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Modicacion de Nombre en Otro Documento", monto=50, duracion_de_tramite=7, procedimiento="Cambio en el Nombre,Cuando el Alumno Ha Realizado su Tramite en Reniec")
tupa_data.save()

#ver esto
#44
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Programa de Aplicacion Profesional", monto=3,300.00, duracion_de_tramite=90 , procedimiento="Asesoramiento para la Sustentacion del PPI")
tupa_data.save()

#45
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Recuperacion de Sustentacion", monto=240.00, duracion_de_tramite=15, procedimiento="Si el Alumno Desaprobo en la Sustentacion,Segunda Opurtunidad")
tupa_data.save()

#46
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Reingreso de Alumno que Abandono", monto=25, duracion_de_tramite=7, procedimiento="Cuando el Alumno Retoma sus Estudios Desde Donde se Quedo,se Adecua a la Malla que este Vigente Maximo 2 Años")
tupa_data.save()

#47
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Reserva de Matricula-Alumno Reingresante y Regular", monto=30, duracion_de_tramite=7, procedimiento="Cuando el Alumno va dejar sus Estudios por un Periodo Maximo de 2 Años")
tupa_data.save()

#48
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Silabos de la Carrera Profesional", monto=110, duracion_de_tramite=7, procedimiento="Silabos por Ciclo,Impresos Sellados y Vizados en Cada Hoja por Direccion General")
tupa_data.save()

#ver esto
#49
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Tramite de Egresado", monto=125, duracion_de_tramite=60, procedimiento="Incluye:Constancia de no Deudor,Record de Notas,Constancia de Egresado,se quedan en el expediente")
tupa_data.save()

#50
tupa_data = tupa(areas_incolucradas="Direccion de Gestion Financiero/Caja", tipo_de_servicio="Transferencia de Pago", monto=25, duracion_de_tramite=7, procedimiento="Pasar el Pago de su Armada a un Familiar")
tupa_data.save()

#ver esto
#50
tupa_data = tupa(areas_incolucradas="Secretaria Académica", tipo_de_servicio="Traslado Externo", monto=0, duracion_de_tramite=15, procedimiento="Tramite que lleva un Proceso para la convalidacion externa del programa con RD")
tupa_data.save()

# INSER TO ADMINS
from myapp_admin.models import Admins

admin_data = Admins(name="Diana Marta", fullname="Pachecco Miraflores", email="useradmin@ils.edu.pe", position="treasury", phone="987365467", dni="7637465", password="password")
admin_data.save()

admin_data = Admins(name="Ana Faviola", fullname="Aguirre Mamani", email="useradmin@ils.edu.pe", position="secretary", phone="987365467", dni="7637465", password="password")
admin_data.save()

admin_data = Admins(name="Luis Roman", fullname="Aguirre Sanchez", email="useradmin@ils.edu.pe", position="direction", phone="987365467", dni="7637465", password="password")
admin_data.save()