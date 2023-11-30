console.log("Que tenemos aquiooooooo");
document.addEventListener('DOMContentLoaded', function() {
	var id_process_btn = document.getElementById("id_process_btn");
	
});


id_process_btn.addEventListener("click", function(){
	const num_boleta = document.getElementById("num_boleta");// NUMERO DEL BAUCHER

	if (num_boleta.value == '') {
		console.log("esta bacio");
	}else{
		process_fut(num_boleta);
	}
})

function process_fut(){
	console.log("la id del fut ees:"+fut_id);
	console.log(chargeAdmin);
	//AJAX
	$.ajax({
	    url: "/process_fut_path/",
	    method: "GET",
	    data:{
	        'fut_id': fut_id,// fut_id ESTA DECLARADO EN view_fut.html
	        'admin_id': admin_id,// fut_id ESTA DECLARADO EN view_fut.html
	        'user_id': user_id,// fut_id ESTA DECLARADO EN view_fut.html
	    },
	    success: function(response){
	        const midata = response; //en response esta recibiendo el return de la funcion
	        console.log(midata);
	        window.location.href = "http://127.0.0.1:8000/ils_admin/staff_treasury";
	    },
	    error: function() {
	        alert("Ocurrió un error al cargar el contenido.");
	    }
	});
}