console.log("CONECTAMOS CON SCRIPT *1233fg");
document.addEventListener('DOMContentLoaded', function() {
	var id_route_content = document.getElementById("id_route_content");
	var id_cont_route = document.getElementById("id_cont_route");
});

function making_tracking_details(mydata, route_fut){
	let left = 0;
	let widt = 20;
	let left_arrow = 30;

	for (var i = 0; i < mydata['length']; i++) {
		console.log("LEONA");
		console.log(mydata);
		var sello_1 = `
			<div class="tra_seal" style="display: block;text-align: center;align-items: center;height: 50px;margin: auto 0px;color: #42AF15;"><h6>PROCESADO</h6><img width="30px" src="/static/img/check.png" alt=""></div>
		`;
		if(mydata[i]["exit"] == null){
			var sello_1 = `
			<div class="tra_seal" style="display: block;text-align: center;align-items: center;height: 50px;margin: auto 0px;color: #464646;opacity: 60%;"><h6>PENDIENTE</h6><img width="30px" src="/static/img/pending.png" alt=""></div>
		`;
		}
		// UN TRACKING
		var ruta = `
			<div id="track_${i}" class="tracking" style="left: ${left}px; width: calc(100% - ${widt}px);margin: 0px;">
	            <div class="tra_info">
	                <h4>${mydata[i]["tittle"]}</h4>
	                <p>${mydata[i]["name"]}__</p>
	                <hr>
	                <p>${mydata[i]["reception"]}</p>
	                <p>${mydata[i]["exit"]}</p>
	            </div>
	            ${sello_1}
	        </div>
	            <div class="arrow" style="left: ${left_arrow}px;"><!---variable iterada y le agregamos 10px mas---->
	                <svg xmlns="http://www.w3.org/2000/svg" id="Capa_1" data-name="Capa 1" viewBox="0 0 83.44 83.44"><defs><style>.cls-1{fill:#ef0033;}</style></defs><title>Captura de pantalla 2023-04-28 155958</title><path class="cls-1" d="M4.77,24.1l3.9-3.91a3.86,3.86,0,0,1,5.48,0l24.55,25a3.86,3.86,0,0,0,5.48,0L69.29,20.17a3.84,3.84,0,0,1,5.45,0l3.93,3.93a3.85,3.85,0,0,1,0,5.48L44.43,63.29a3.86,3.86,0,0,1-5.42,0L4.79,29.58A3.85,3.85,0,0,1,4.77,24.1Z"/></svg>
	            </div>
		`;
		id_route_content.innerHTML += ruta;

		//CAMBIAMOS LAS VARIABLES
		left = left + 20;
		widt = widt + 20;
		left_arrow = left_arrow + 20;
	}
	var finished_html = `
		<div class="message_finished_cont">
            <img src="/static/img/finished.png" alt="">
           <h3>¡TRAMITE FINALIZADO!</h3>
           <P>ahora puede descargar el tramite o acercarse a la institución educativa</P>
           <p>para que se le imprima en el formato requerido.</p>
        </div>
	`;

	if(route_fut == 'finished'){
		id_route_content.innerHTML += finished_html;
		estado_fut();
	};

	//add_observation(mydata['length']);
}

function add_observation(num){
	num = num -1;
	let html_label = `
		<div class="label_observation">
			<img src="/static/img/alert.png">
		</div>
	`;
	document.getElementById("track_"+num).innerHTML += html_label;
	document.getElementById("track_"+num).classList.add("observation");
}

function obtain_get_tracking(){
	return new Promise(function (resolve, reject) {
		//AJAX
		$.ajax({
		    url: "/tracking_path/",
		    method: "GET",
		    data:{
		        'id_fut':id_fut,// VARIABLE DEFINIDA EN proceedings.html
		    },
		    success: function(response){
		        const midata = response; //en response esta recibiendo el return de la funcion
		        resolve(midata['data']);
		    },
		    error: function() {
		        alert("Ocurrió un error al cargar el contenido.");
		    }
		});
	});
}

// AQUI OBTENEMOS LOS DETALLES DE SEGUIMIENTO
async function get_tracking(route_fut){
	console.log("01_TRACKING");
	var mydata = await obtain_get_tracking();
	making_tracking_details(mydata, route_fut);
}

function obtain_pross_route(){
	return new Promise(function (resolve, reject) {
		//AJAX
		$.ajax({
		    url: "/pros_route_path/",
		    method: "GET",
		    data:{
		        'id_fut':id_fut,// VARIABLE DEFINIDA EN proceedings.html
		    },
		    success: function(response){
		        const midata = response; //en response esta recibiendo el return de la funcion
		    	resolve(midata['route']);
		    },
		    error: function() {
		        alert("Ocurrió un error al cargar el contenido.");
		    }
		});
	});
}

// AQUI DETERMINAREMOS EL  FUNCIONAMIENTO DE CUANDO FINALIZA O NO EL FUT
function estado_fut(){
	document.getElementById("state").innerHTML=`<p>Estado</p><p style="color: green;">Finalizado</p>`;
	document.getElementById("idadvertencia").classList.add("cambio_finished");
	document.getElementById("idadvertencia").innerHTML=`
	<img src="/static/img/finished_blue.png" alt="">
    <p>El tramite a finalizado. Si desea que se imprima acerquese al instituto y brinde el número de Expediente.</p>
    <a href="">más información</a>
	`;
	document.getElementById("id_doc_download").classList.add("doc_finaliced");
	document.getElementById("id_doc_download").innerHTML = `
	<img src="/static/img/doc.png" alt="">
	<p class="btn_down" onclick="btn_download()">Descargar</p>
	`;
	// ---------------------------
	let data_doc = `
	<div class="d_document">
        <p>Disponibilidad de descarga:</p>
        <p class="num_data_doc" style="color: green;">Publico</p>
    </div>
    <div class="d_document">
        <p>Origen:</p>
        <p class="num_data_doc">Instituto ILS</p>
    </div>
    <div class="d_document">
        <p>Numero de paginas:</p>
        <p class="num_data_doc">1</p>
    </div>
    <div class="d_document">
        <p>Tamaño:</p>
        <p class="num_data_doc">250KB</p>
    </div>
    <div class="d_document">
        <p>Formato:</p>
        <p class="num_data_doc">pdf</p>
    </div>
	`;
	document.getElementById("la_data_doc").innerHTML = data_doc;
}

get_route();
// AQUI OBTENEMOS LA RUTA DE TRAMITE
async function get_route(){
	console.log("GET_ROUTE");
	var route_fut  = await obtain_pross_route();// OBTENEMOS ESTA VARIABLE DEL MODELO FUT (para saber como pintar la ruta)
	get_tracking(route_fut);
	// OBTENEMOS EL on Y off PARA PINTAR
	var diccionario_circle = list_circles(route_fut);
	var diccionario_line = list_lines(route_fut);
	// PINTAMOS RUTA DE TRAMITE
	macking_route(diccionario_circle, diccionario_line);
}

function macking_route(diccionario_circle, diccionario_line){
	id_cont_route.innerHTML = "";
	for (var i = 1; i < 6; i++) {
		var html_route = `
			<div class="circle">
	            <img width="100%" src="/static/img/process/${diccionario_circle[i]}" alt="">
	        </div>
		`;
		id_cont_route.innerHTML += html_route;
		if(i<5){
			id_cont_route.innerHTML += `<div id="id_line_${i}" class="ProgressBar"></div>`;
			add_line(i, diccionario_line[i]);
		}
	};
}

function add_line(num, suitck){
	for (var i = 0; i < 8; i++) {
		document.getElementById("id_line_"+num).innerHTML += `<div class="progre ${suitck}"></div>`;
	}
}

function list_circles(route){
	let miDiccionario2 = {};

	miDiccionario2[1] = "P_01-on.png";
	miDiccionario2[2] = "P_02-on.png";

	if(route == 'treasury'){
		miDiccionario2[3] = "P_03-off.png";
		miDiccionario2[4] = "P_04-off.png";
		miDiccionario2[5] = "P_05-off.png";
	}else if(route == 'secretary'){
		miDiccionario2[3] = "P_03-on.png";
		miDiccionario2[4] = "P_04-off.png";
		miDiccionario2[5] = "P_05-off.png";
	}else if(route == 'direction'){
		miDiccionario2[3] = "P_03-on.png";
		miDiccionario2[4] = "P_04-on.png";
		miDiccionario2[5] = "P_05-off.png";
	}else{// route == finished
		miDiccionario2[3] = "P_03-on.png";
		miDiccionario2[4] = "P_04-on.png";
		miDiccionario2[5] = "P_05-on.png";
	}
	return miDiccionario2;
}

function list_lines(route){
	let miDiccionario = {};

	miDiccionario[1] = "on";

	if(route == 'treasury'){
		miDiccionario[2] = "off";
		miDiccionario[3] = "off";
		miDiccionario[4] = "off";
	}else if(route == 'secretary'){
		miDiccionario[2] = "on";
		miDiccionario[3] = "off";
		miDiccionario[4] = "off";
	}else if(route == 'direction'){
		miDiccionario[2] = "on";
		miDiccionario[3] = "on";
		miDiccionario[4] = "off";
	}else{// route == finished
		miDiccionario[2] = "on";
		miDiccionario[3] = "on";
		miDiccionario[4] = "on";
	}
	return miDiccionario;
}

view_fut();
function view_fut(){
	console.log("YA SE VIO");
	$.ajax({
    	url: "/view_fut_path/",
    	method: "GET",
    	data:{
        	'id_fut':id_fut,// VARIABLE DEFINIDA EN proceedings.html
    	},
    	success: function(response){
        	const midata = response; //en response esta recibiendo el return de la funcion
        	console.log(midata);
    	},
    	error: function() {
        	alert("Ocurrió un error al cargar el contenido.");
    	}
	});
}
import { establecerCookie } from '/static/scripts/cookies.js';
// BOTÓN ABRIR OBSERVACIONES
document.getElementById("open_observations").addEventListener('click', function(){
	// open_observations();
	establecerCookie('fut_id', id_fut)// id_fut FUE DEFINIDA EN proceedings.html
	establecerCookie('fut_order', order_fut)// order_fut FUE DEFINIDA EN proceedings.html
	window.location.href = link_observation;// link_observation FUE DEFINIDA EN proceedings.html
});