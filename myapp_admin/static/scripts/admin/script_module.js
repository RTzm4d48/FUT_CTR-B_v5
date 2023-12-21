document.addEventListener('DOMContentLoaded', function() {
	var id_process_btn = document.getElementById("id_process_btn");
	var id_btn_public = document.getElementById("id_btn_public");
	var id_btn_process_secretary = document.getElementById("id_btn_process_secretary");
	
});

import { process_fut, paint_file, get_file_fron_db } from './script_procesos.js';

// TESORERIA - PROCESAR TRAMITE
id_process_btn.addEventListener("click", function(){
	const num_boleta = document.getElementById("num_boleta");// NUMERO DEL BAUCHER

	if (num_boleta.value == '') {
		alert("Ingrese el número del Baucher")
	}else{
		process_fut('secretary');// LA VARIABLE ES PARA ACTUALIZAR LA ruta de FUT
	}
})

//SECRETARIA - PROCESAR TRAMITE
document.getElementById("fileUploadForm").addEventListener('submit', function(event) {
	const description = document.getElementById("description_general").value;// DESCRIPCIÓN
	const select_pdf = document.getElementById("select_pdf").value;// Input Hidden para saber si se subio un archivo
	if (description == "") {
		event.preventDefault();
		alert("ingrese la descripcion del documento.");
	}else if(select_pdf == ""){
		event.preventDefault();
		alert("Seleccione un archivo pdf.");
	}else{
		console.log("SE ENVIO EL FORMULARIO");
		process_fut('direction');// LA VARIABLE ES PARA ACTUALIZAR LA ruta de FUT
	}
});

// DIRECTOR - PUBLICAR TRAMITE
document.getElementById("upload_direction").addEventListener('submit', function(event) {
	let num_exp = document.getElementById("num_expediente").value;
	let select_pdf = document.getElementById("select_pdf_direction").value;
	
	if (num_exp == "") {
		event.preventDefault();
		alert("Por favor ingrese el número de Expediente");
	}else if(select_pdf == ""){
		event.preventDefault();
		alert("Por favor seleccione el documento pdf firmado.");
	}else{
		console.log("SE ENVIO EL FORMULARIO en dirección");
		process_fut('finished');// LA VARIABLE ES PARA ACTUALIZAR LA ruta de FUT
	}
});

var ff = document.getElementById("pdf_file2_2");
ff.addEventListener('change', function(event){
    // Obtener la lista de archivos seleccionados
    var archivos = event.target.files;

    // Hacer algo con los archivos seleccionados
    for (var i = 0; i < archivos.length; i++) {
        const name = archivos[i].name;
    	document.getElementById("text_pdfFile").innerHTML = paint_file(name);
    	document.getElementById("select_pdf").value = "true";
    }
});

var pdf_file_direction = document.getElementById("pdf_file_direction");
pdf_file_direction.addEventListener('change', function(event){
    // Obtener la lista de archivos seleccionados
    var archivos = event.target.files;

    // Hacer algo con los archivos seleccionados
    for (var i = 0; i < archivos.length; i++) {
        const name = archivos[i].name;
    	document.getElementById("txt_pdf_direct").innerHTML = paint_file(name);
    	document.getElementById("select_pdf_direction").value = "true";
    }
});

// PARA QUE DIRECCION DESCARGUE EL DOCUMENTO PROCESADO POR LA SECRETARIA
document.getElementById("btn_download_doc").addEventListener('click', function(){
	get_file_fron_db();
});

