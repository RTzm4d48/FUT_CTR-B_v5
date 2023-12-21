console.log("es lo necesario 3");

function observations(){

}

import { get_db_ticket, paint_tickets, paint_messages_tickets, obtain_ticket_desarrollo } from './script_module.js';

// COOKIE MANAGE
import { obtenerValorCookie } from '/static/scripts/cookies.js';

// ABRIR OBSERVACIONES
export async function open_observations(charge){
	//OBTENEMOS LA ID DEL TICKET
	let fut_id = obtenerValorCookie('fut_id');
	// OBTENEMOS LOS TICKETS
	var ticket_data = await get_db_ticket(charge, fut_id);// ENVIAMOS EL CHARGE COMO PARAMETRO
	
	// ESCRIBIMOS EL HTML DE LOS TICKETS
	paint_tickets(ticket_data);
}

// ESTILOS DEL NAV BAR
export function style_navbar(direction){
	if (direction == "observation") {
		// ICON
		document.getElementById("id_img_1").src = "/static/img/rep_white.png";
		// CLASS
		document.getElementById("id_item_1").classList.add("item_active");

	}else if(direction == "ticket"){
		// ICON
		document.getElementById("id_img_2").src = "/static/img/pngegg_white.png";
		// CLASS
		document.getElementById("id_item_2").classList.add("item_active");
	}else{
		// ICON
		document.getElementById("id_img_3").src = "/static/img/direction.png";
		// CLASS
		document.getElementById("id_item_3").classList.add("item_active");
	}
}

// EN ESTA FUUNCIÓN MANEJAREMOS LA RUTA
export 	function manage_rute(route){
		var id_rute = document.getElementById("main_rute");
		id_rute.innerHTML = "";

		var length = route['length'];
		for (var i = 0; i < length; i++) {
			// VARIABLES
			let name = route[i];

			id_rute.innerHTML += `<p class="ruta">${name}</p>`;
			var o = i+1;
			if (o == length) {break;}
			id_rute.innerHTML += `<p class="simbolo">&gt;</p>`;

		}
}

export async function messages_ticket(id_ticket){
	var data_desarrollo = await obtain_ticket_desarrollo(id_ticket);
	paint_messages_tickets(data_desarrollo);
	
}


export function prueba_m(name){
	console.log("hola "+name);
}