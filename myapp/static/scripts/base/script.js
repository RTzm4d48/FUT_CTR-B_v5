console.log("CONECTAMOS CON SCRIPT *123ss");
document.addEventListener('DOMContentLoaded', function() {
	var id_message = document.getElementById("id_message");
	var id_desplegable_message = document.getElementById("id_desplegable_message");
	//CONT GENERAL DEL LAS NOTIFICACIONES MESSAGE
	var cont_general_msge = document.getElementById("cont_general_msge");
	var cont_general_moti = document.getElementById("cont_general_moti");

});

//document.addEventListener("scroll", bloquearScroll);

import { create_pop_notifi, insertNotificaction } from './ticket_notification.js';

cont_general_msge.addEventListener('click', function(){
	
	window.miVariable;
	if(window.miVariable == false){
		window.miVariable = true;
		cerrar_pop_mssg();
	}else{
		cerrar_pop_mssg();
		window.miVariable = false;
		create_pop();
	}
});

cont_general_moti.addEventListener('click', function(){
	
	window.suitch2;
	if(window.suitch2 == false){
		window.suitch2 = true;
		cerrar_pop_mssg();
	}else{
		cerrar_pop_mssg();
		window.suitch2 = false;
		create_pop_notifi();
	}
});

function bloquearScroll(event) {
    // Evitar el comportamiento por defecto del evento de desplazamiento
    event.preventDefault();
    console.log("d");
    cerrar_pop_mssg();
}

function create_pop(){
	var noti_html = `
		<img src="/static/img/message.png" alt="">
        <!-- - -->
        <div id="id_desplegable_message" class="desplegable_content">
        	<div class="nav_desp">
            	<div class="lado">
            	Tickets
            	</div>
            	<div class="lado">
            		<img class="closeImg" src="/static/img/close.png">
            	</div>
        	</div>
        	<div id="content_not_princip" class="content_Desp">
            	<div class="empty_desp">
            	<p>Aqui no hay Nada.</p>
            	</div>
        	</div>
        </div>
	`;

	cont_general_msge.innerHTML = noti_html;
	insertNotificaction("/get_message_ticket_path/", "ticket");
}

function cerrar_pop_mssg(){
	var noti_html = `
		<img src="/static/img/message.png" alt="">
	`;
	var noti_hrml2 = `
		<img src="/static/img/bell.png" alt="">
	`;

	cont_general_msge.innerHTML = noti_html;// TICKETS
	cont_general_moti.innerHTML = noti_hrml2;// NOTIFICACIONES

	// CAMBIAMOS LAS VARIABLES DE LOS SWITCHS
	window.suitch2 = true;
	window.miVariable = true;
}

