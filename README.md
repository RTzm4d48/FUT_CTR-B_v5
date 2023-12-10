<p align="center">
    <br>
    <img src="https://github.com/Edgar-ae/FUT_CTR-B_v5/blob/main/static/project_logo.png" width="400"/>
    <br>
<p>

# FUT_CTR-B - Sistema de Formulario Unico de Tramite

## Guia de instalacion de mi sistema web FUT en el servidor de Apache


Para poder iniciar con la instalación del sistema en el servidor tenemos que crear un entorno virtual.
Basicamente creamos una carpta y allí instalamos todo lo que necesitemos como python, pip, modulos, dependencias, etc.

Para ello nos ubicamos en la carpeta de nuestro proyecto y crearemos el entorno virtual llamado `virtualenv`. Este en un modulo de pip

    pip install virtualenv

ahora crearemos una carpeta llamada venv. Ahí estará nuestro proyecto

    virtualenv venv

### Activamos la virtualización

    source venv/bin/activate

## Instalar Django

Ahora insrtalare Djando en mi entorno virtual.

    pip install django

Para conprovar que ya tengo django hago esto.

~~~
python -m django --version
~~~

    django-admin --version

~~~
python
import django
django.get_version()

exit()
~~~

### configuración de Apache

~~~
<VirtualHost *:80>
    ServerAdmin mi@email.com
    ServerName FUT
    DocumentRoot http://localhost:8000/

    WSGIDaemonProcess FUT_CTR-B_v6 python-home=http://localhost:8000//venv python-path=http://localhost:8000/
    WSGIProcessGroup FUT_CTR-B_v6
    WSGIScriptAlias / http://localhost:8000/FUT_CTR-B_v6/wsgi.py

    <Directory http://localhost:8000/FUT_CTR-B_v6>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    Alias /static/ http://localhost:8000/FUT_CTR-B_v6/static/
    <Directory http://localhost:8000//FUT_CTR-B_v6/static>
        Require all granted
    </Directory>

    Alias /media/ http://localhost:8000/FUT_CTR-B_v6/media/
    <Directory http://localhost:8000/FUT_CTR-B_v6/media>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
~~~

### Instalar requerimientos

si es que hemos hecho clone de un proyecto existente en github, tenemos que instalar los requerimientos y lo hacemos de la sigiente manera

    pip install -r requirements.txt

y si quieremos crar o actualizar nuestro archivo de requerimientos lo podemos hacer con esto

    pip freeze > requirements.txt

---
   
Ahora con el entono virtual activado podremos instalar modulos solo en la carpeta de nuestro proyecto y no el systema de nuestra PC

## Migraciones

Ahoa nos ubicamos en nuestro entorno virtual y ejecutamos las migraciones

    python manage.py migrate


Ahora ejecutaremos la makemigrations y esto creara un archivo en `./myapp/migrations/0001_initial.py` lo que hara este archivo por nostros es crear las tablas. Este archivo no hay que tocarlom, es solo para ver.

    python manage.py makemigrations myapp

Bien ahora vamos a ejecutar ese archivo con:

    python manage.py migrate myapp

## Django Admin

para administrar el proyecto podemos entrar a `http://127.0.0.1:3000/admin` o `localhost:3000/admin` ahí nos pedira un usuario. Nosotros podremos crearlo en (DB Browser for SQLite) en el apartado `auth_user` de la BD  


Pero no usaremos el software, lo haremos mediante la consols usando `manage.py`

    python manage.py createsuperuser

pocedimiento en consola

~~~
(venv) E:\_TALLER_\django_project>python manage.py createsuperuser
Username (leave blank to use 'edgar'): edgar
Email address: edgar@gmail.com
Password:
Password (again):
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(venv) E:\_TALLER_\django_project>
~~~

entonces iniciamos el servidor nevamente `python manage.py runserver` y nos logueamos

# Requerimientos

Aqui muestro los requerimientos que se encuantra en la carpeta `requirements.txt` de mi proyecto.

~~~
asgiref==3.6.0
beautifulsoup4==4.12.2
cachetools==5.3.1
certifi==2023.5.7
charset-normalizer==3.1.0
colorama==0.4.6
cssselect==1.2.0
cssutils==2.7.0
distlib==0.3.7
Django==4.2
django-bootstrap4==23.1
dkimpy==1.1.4
dnspython==2.3.0
filelock==3.12.2
idna==3.4
importlib-metadata==6.6.0
jaraco.classes==3.2.3
keyring==23.13.1
lxml==4.9.2
more-itertools==9.1.0
numpy==1.24.3
opencv-python-headless==4.7.0.72
platformdirs==3.10.0
premailer==3.10.0
pypng==0.20220715.0
python-dotenv==0.20.0
pywin32-ctypes==0.2.0
qrcode==7.4.2
requests==2.31.0
soupsieve==2.4.1
sqlparse==0.4.4
typing-extensions==4.5.0
tzdata==2023.3
urllib3==2.0.3
virtualenv==20.24.2
win32-setctime==1.1.0
yagmail==0.15.293
zipp==3.15.0
~~~
