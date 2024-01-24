export async function get_db_ticket(charge, fut_id){
	return new Promise(function(resolve, reject){
		console.log("que paso jefe_4");
		//AJAX
		$.ajax({
		    url: "/get_db_ticket_path/",
		    method: "GET",
		    data:{
		    	'charge': charge,
		    	'fut_id': fut_id
		    },
		    success: function(response){
		        const midata = response;
		        console.log(midata);
		        resolve(midata);
		    },
		    error: function() {
		        alert("Ocurrió un error al cargar el contenido.");
		    }
		});
	});
}

export function paint_tickets(ticket_data, charge){
	console.log("REMEMBER");
	console.log(ticket_data);
	if(ticket_data['data']['length'] == 0){
		// var impty_html = ``;
		document.getElementById("cont_low_register").innerHTML = `
		<h3 class="empty">Esta lista esta bacia...</h3>
		<button id="btn_create_new_ticket" onclick="createticket()" class="btn_create_ticket"><img src="/static/img/plus_white.png">Crear un nuevo ticket</button>`;
		// LA ID cont_register ESTA EN templates\view_fut\observations\show.html
		document.getElementById("cont_register").innerHTML = impty_html;
	}else{
		document.getElementById("cont_register").innerHTML = "";
		for(let i=0; i<ticket_data['data']['length']; i++){
			//VARIABLES
			let tittle = ticket_data['data'][i]['tittle'];
			let code = ticket_data['data'][i]['code'];
			let charge = ticket_data['data'][i]['charge'];
			var register_html = `
				<a href="/my_fut/observation/show_redirect/${code}/${charge}/">
					<div class="register">
						<img src="/static/img/rep_black.png" alt="">
						<p>${tittle}</p>
						<p style="margin:auto 5px;color:#727272;">(${charge})</p>
						<P style="margin:auto 10px auto auto;">Code: ${code}</P>
					</div>
				</a>
			`;
			document.getElementById("cont_register").innerHTML += register_html;
		}
		document.getElementById("cont_low_register").innerHTML = `<button id="btn_create_new_ticket" onclick="createticket()" class="btn_create_ticket"><img src="/static/img/plus_white.png">Crear un nuevo ticket</button>`;
	}
}

export function paint_messages_tickets(data){
	let tittle = data['only_this_ticket']['tittle'];
	let num_ticket = data['only_this_ticket']['num_ticket'];
	let charge = data['only_this_ticket']['charge'];
	var cont_message_html = `
			<div class="cont_message">
				<div class="davbbar">
					<img class="atras" src="/static/img/atras.png">
					<img src="/static/img/rep_black.png">
					<p>${tittle}</p>
					<p style="margin:auto 5px;color:#727272;">(${charge})</p>
					<p style="margin: auto 5px auto auto">Num: ${num_ticket}<p>
				</div>
				<div id="cont_main_message" class="cont_main_message">
				</div>
				<button onclick="create_desarrollo()" class="respoder"><img src="/static/img/reply_red.png">Responder</button>
			</div>
			`;
			document.getElementById("cont_register").innerHTML = cont_message_html;
	for (var i = 0; i < data['data']['length']; i++) {
		console.log(data['data'][i]['charge'])
		// VARIABLES
		let tittle = data['data'][i]['name'];
		let desarrollo = data['data'][i]['desarrollo'];
		let charge = data['data'][i]['charge'];
		let id = data['data'][i]['id'];
		let date = calcularTiempoTranscurrido(data['data'][i]['date']);
		
		var message_html = `
					<div class="block">
						<div id="id_img_space_${i}">
							<img class="user_img" src="/static/img/admin_icon.png" alt="">
						</div>
						<h4>${tittle}</h4>
						<p style="margin: auto 5px auto 10px;color:gray">${date}</p>
					</div>
					<div class="block text_space">
						<p>${desarrollo}</p>
						<div class="cont_img_desarrollo">
							<img class="img_desarrollo" src="/static/tmp/desarrollo_attach_${id}.jpg" alt="">
							<div onclick="show_img(${id})" class="elHoverDeImg">
								<img class="zoom_icon" src="/static/img/zoom_icon.png" alt="">
							</div>
						</div>
					</div>
					<div class="block text_space">
						<div id="sello_${i}">
						</div>
					</div>
					<hr style="margin:15px auto;">
			`;
			document.getElementById("cont_main_message").innerHTML += message_html;

			if(charge == "alumno"){
				document.getElementById("sello_"+i).innerHTML = ``;
				document.getElementById("id_img_space_"+i).innerHTML = `<img class="user_img" src="/static/img/profile_user_test.jpg">`;
			}else{
				let stamp = charge == "Tesorera" ? "stamp_treasury" : (charge == "Secretaria" ? "stamp_secretary" : "stamp_direction");
				document.getElementById("sello_"+i).innerHTML = `<img class="img_identification" src="/static/img/stamp/${stamp}.png">`;
			}
		}
}
import moment from 'https://cdn.skypack.dev/moment';
function calcularTiempoTranscurrido(fecha) { // fecha es un datetime '2023-11-28 14:57:15'
	//var moment = require('moment');
	var dateCleaned = fecha.replace('T', ' ').replace('Z', '');
	const fechaActual = moment();
	const fechaDada = moment(dateCleaned);

	const minutosTranscurridos = fechaActual.diff(fechaDada, 'minutes');
	const horasTranscurridas = fechaActual.diff(fechaDada, 'hours');
	const diasTranscurridos = fechaActual.diff(fechaDada, 'days')

	const fechaActual2 = moment();
	const formatoPersonalizado = fechaActual2.format('YYYY-MM-DD HH:mm:ss');

	if (minutosTranscurridos < 60) {
	  return `Hace ${minutosTranscurridos} minutos`;
	} else if (horasTranscurridas < 24) {
	  return `Hace ${horasTranscurridas} horas`;
	} else {
	  return `Hace ${diasTranscurridos} días`;
	}
}
//ESTO AUN NO SE USA PERO YA VEREMOS
function obtain_i_url(){
	// Obtener la URL actual
	let urlString = window.location.href;

	// Crear un nuevo objeto URLSearchParams con la URL
	let urlParams = new URLSearchParams(urlString.split('?')[1]);

	// Obtener el valor de la variable 'i'
	let valorI = urlParams.get('i');
	return valorI
}

export function obtain_ticket_desarrollo(id_ticket){
	return new Promise(function(resolve, reject){
		//AJAX
		$.ajax({
		    url: "/get_desarrollo_db_path/",
		    method: "GET",
		    data:{
		        'id_ticket':id_ticket,
		    },
		    success: function(response){
		        const midata = response;
		        resolve(midata);
		    },
		    error: function() {
		        alert("Ocurrió un error al cargar el contenido.");
		    }
		});
	})
}