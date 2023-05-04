# FUT_CTR-B - Guia

Breve descripción del proyecto.

## Captura de referancia

![image](./img/)

## Informacion importante

- Use **Django** como framework de dasarrollo

- Crei que **jinja** me estaba dando muchos problemas pero en realidad no estaba usando el motor de pantillas **jinja** sino que era el que venia por defecto con django **Django Templates**

- El motor de plantillas **Django Templates** tiene limitaaciones en cuanto a la realisacion de operaciones aritmeticas con las varialbes y en general

- Aprendi que cuando hacemos un **commit** con **git** no se incluye la carpeta **venv** del **entorno virtual** ya que esto es redundante y aumenta innecesariamente el peso de nuestro peoyecto. Se suguiere que cada desarrollador haga un clone del proyecto y descargue solo las librerias que vaya a usar. en liugar de **venv** se debera crear un archivo **'requirements.txt'** en donde se muestre todas las librerias que se esta usando en el proyecto.

### Herramientas usadas

- **Django** como framework de dasarrollo

- **Django Templates** como Motor de plantillas

### bibiografia

[link]()

## Linea de tienpo

> 1. paso 1

## HELPER

En este apartado veremos frangometos de herramientas o funciones que use en el desarrolo de esté
pryecto, los cuales considero importante recordad por lo cual hago una pequeña guia bien desarrollada

### Requerimientos instalados en en entorno virtaual

> 1. Mediante un comando por consola se creara un archivo .txt en donde se enlistara todos los paquetes que tenemos instalado en nuestro entorno virtual

> 2. Para crear el archivo 'requirements.txt', puede redirigir la salida del comando pip freeze a un archivo llamado 'requirements.txt' utilizando el símbolo de mayor que (>). Por ejemplo, en una terminal con el entorno virtual 'venv' activado, puede ejecutar el siguiente comando:

    pip freeze > requirements.txt

### Ventana Emergente (Login)

> 3. Crea un botón de inicio de sesión en la página principal de tu sitio web, que activará la ventana emergente cuando se haga clic en él.

```html
<button onclick="openLoginForm()">Iniciar sesión</button>
```
> 4. Crea la ventana emergente de inicio de sesión en tu archivo HTML utilizando la etiqueta div

```html
<div id="login-form-popup">
  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Nombre de usuario">
    <input type="password" name="password" placeholder="Contraseña">
    <input type="submit" value="Iniciar sesión">
  </form>
</div>
```
> 5. lo que me parece clave para las ventanas emergentes y para el navbar son estas propiedades css

```css
#login-form-popup {
  display: none;
  position: fixed; /* para que no se mueva conel scroll */
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}
```

> 6. Use JavaScript para manegar la fucionalidad del botton loguin y en manejo de la ventana de loguin. Aqui mostrare un poco de codigo solo para guiar.

```js
function openLoginForm() {
  document.getElementById("login-form-popup").style.display = "block";
}

window.onclick = function(event) {
  if (event.target == document.getElementById("login-form-popup")) {
    document.getElementById("login-form-popup").style.display = "none";
  }
}
```

### MEDIA_ROOT o carpeta de medios

> 1. Esta carpeta no la conocia del todo pero basicamente es para almacenar (imágenes, vídeos, documentos, etc) y **'MEDIA_ROOT'** está configurado para almacenar estos archivos. Y lo podemos configurar de la siguiente manera.

> 2. agregamos esta linea de código en el archivo **(`'settings.py'`)**

```py
import os
# Los archivos de multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'myapp\media')
```
 
así media **'MEDIA_ROOT'** contiene la siguente dirección: (E:\ _TALLER_\FUT_CTR-B_v3\myapp\media\image.jpg)

> 3. Como ejemplo para descargar una imagen GPT me dio el siguiente query:

Para descargar una imagen mediante un botón en un proyecto de Django, puedes seguir los siguientes pasos:

1. Crear una vista en Django que permita la descarga de la imagen. Esta vista debe recibir como parámetro el nombre de la imagen que se desea descargar.

2. Crear una URL en el archivo urls.py del proyecto que apunte a la vista creada en el paso anterior. Esta URL debe contener el parámetro que se le va a pasar a la vista.

3. Crear un botón en el template HTML que llame a la URL creada en el paso anterior. Este botón debe tener la etiqueta a y el atributo href debe apuntar a la URL.

4. Crear una vista en Django que permita la descarga de la imagen. Esta vista debe abrir el archivo de la imagen y devolverlo al usuario utilizando el método HttpResponse.

Aquí te dejo un ejemplo de cómo podrías implementar la vista en Django para descargar la imagen:

```python
from django.http import HttpResponse
from django.conf import settings
import os

def download_image(request):
    image_name = 'image.jpg'
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="%s"' % image_name
        return response
```

En este ejemplo, se utiliza la variable MEDIA_ROOT de Django para obtener la ruta absoluta donde se encuentra la imagen que se quiere descargar. La vista utiliza el método open para abrir el archivo y devolverlo como respuesta HTTP con el content_type 'image/jpeg' y el Content-Disposition 'attachment' para indicar que se quiere descargar el archivo.


### 