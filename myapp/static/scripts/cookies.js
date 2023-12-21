// CREAR COOKIE
export function establecerCookie(nombre, valor) {
    // Crear la fecha de expiración para la cookie (opcional).
    var fechaExpiracion = new Date();
    fechaExpiracion.setDate(fechaExpiracion.getDate() + 1); // Caduca en 1 día

    // Construir la cadena de la cookie.
    var cookieString = nombre + "=" + valor + "; expires=" + fechaExpiracion.toUTCString() + "; path=/";

    // Establecer la cookie.
    document.cookie = cookieString;
}

// PARA VALIDAR SI EXISTE O NO UNA COOKIE
export function existeCookie(nombre) {
    // Obtiene todas las cookies del documento y las divide en un array.
    var cookies = document.cookie.split(';');

    // Itera sobre las cookies para buscar la que tiene el nombre específico.
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Verifica si la cookie comienza con el nombre específico.
        if (cookie.indexOf(nombre + "=") === 0) {
            // La cookie existe.
            return true;
        }
    }

    // La cookie no fue encontrada.
    return false;
}

// PARA OBTENER UNA COOKIE
export function obtenerValorCookie(nombre) {
    // Obtiene todas las cookies del documento y las divide en un array.
    var cookies = document.cookie.split(';');

    // Itera sobre las cookies para buscar la que tiene el nombre específico.
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Verifica si la cookie comienza con el nombre específico.
        if (cookie.indexOf(nombre + "=") === 0) {
            // Retorna el valor de la cookie.
            return cookie.substring(nombre.length + 1, cookie.length);
        }
    }

    // La cookie no fue encontrada.
    return null;
}

// PARA ELIMINAR UNA COOKIE
export function eliminarCookie(nombre) {
    // Establecer la fecha de expiración en el pasado.
    var fechaExpiracion = new Date();
    fechaExpiracion.setFullYear(fechaExpiracion.getFullYear() - 1);

    // Construir la cadena de la cookie con fecha de expiración en el pasado.
    var cookieString = nombre + "=; expires=" + fechaExpiracion.toUTCString() + "; path=/";

    // Establecer la cookie para eliminarla.
    document.cookie = cookieString;
}

export function prueba(name){
	alert("hola "+name);
}