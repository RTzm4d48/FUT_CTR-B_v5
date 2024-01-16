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
	console.log("PAIINTER__3");
	console.log(ticket_data['data']['length']);
	if(ticket_data['data']['length'] == 0){
		// var impty_html = ``;
		document.getElementById("cont_low_register").innerHTML = `
		<h3 class="empty">Esta lista esta bacia...</h3>
		<button id="btn_create_new_ticket" onclick="createticket()" class="btn_create_ticket"><img src="/static/img/plus_white.png">Crear un nuevo ticket</button>`;
		document.getElementById("cont_register").innerHTML = impty_html;
	}else{
		document.getElementById("cont_register").innerHTML = "";
		for(let i=0; i<ticket_data['data']['length']; i++){
			//VARIABLES
			let tittle = ticket_data['data'][i]['tittle'];
			let code = ticket_data['data'][i]['code'];
			var register_html = `
				<a href="/my_fut/observation/show_redirect/${code}/${charge}/">
					<div class="register">
						<img src="/static/img/rep_black.png" alt="">
						<p>${tittle}__</p>
					</div>
				</a>
			`;
			document.getElementById("cont_register").innerHTML += register_html;
		}
		document.getElementById("cont_low_register").innerHTML = `<button id="btn_create_new_ticket" onclick="createticket()" class="btn_create_ticket"><img src="/static/img/plus_white.png">Crear un nuevo ticket</button>`;
	}
}

export function paint_messages_tickets(data){
	var cont_message_html = `
			<div class="cont_message">
				<div class="davbbar">
					<img class="atras" src="/static/img/atras.png">
					<img src="/static/img/rep_black.png">
					<p>Se adjunto la foto del baucher icorrectamente _</p>
				</div>
				<div id="cont_main_message" class="cont_main_message">
				</div>
				<button onclick="create_desarrollo()" class="respoder"><img src="/static/img/reply_red.png">Responder</button>
			</div>
			`;
			document.getElementById("cont_register").innerHTML = cont_message_html;	
	console.log("PHONK_2");
	console.log(data);

	for (var i = 0; i < data['data']['length']; i++) {
		console.log(data['data'][i]['charge'])
		// VARIABLES
		let tittle = data['data'][i]['name'];
		let desarrollo = data['data'][i]['desarrollo'];
		let charge = data['data'][i]['charge'];

		var message_html = `
					<div class="block">
						<div id="id_img_space_${i}">
							<img class="user_img" src="/static/img/admin_icon.png" alt="">
						</div>
						<h4>${tittle}</h4>
					</div>
					<div class="block text_space">
						<p>${desarrollo}</p>
					</div>
					<div class="block text_space">
						<div id="sello_${i}">
						</div>
					</div>
					<hr style="margin:15px auto;">
			`;
			document.getElementById("cont_main_message").innerHTML += message_html;

			if(charge == "(alumno)"){
				document.getElementById("sello_"+i).innerHTML = ``;
				document.getElementById("id_img_space_"+i).innerHTML = `<img class="user_img" src="/static/img/profile_user_test.jpg">`;
			}else{
				document.getElementById("sello_"+i).innerHTML = `<img class="img_identification" src="/static/img/tesoreria_identification.jpg">`;
			}
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