// ENVIAMOS EL FUT AL SIGUIENTE ADMIN Y ACTUALIZAMOS LO NECESARIO
export function process_fut(route, num_boleta){
  //AJAX
  console.log("queeee:");
  console.log(num_boleta);
  $.ajax({
      url: "/process_fut_path/",
      method: "GET",
      data:{
          'fut_id': fut_id,// fut_id ESTA DECLARADO EN view_fut.html
          'admin_id': admin_id,// fut_id ESTA DECLARADO EN view_fut.html
          'user_id': user_id,// fut_id ESTA DECLARADO EN view_fut.html
          'route': route,// para actualizar el fut
          'num_boleta': num_boleta
      },
      success: function(response){
          const midata = response; //en response esta recibiendo el return de la funcion
          console.log(midata);
          //window.location.href = "http://127.0.0.1:8000/ils_admin/staff_treasury";
      },
      error: function() {
          alert("Ocurrió un error al cargar el contenido.");
      }
  });
}

export function paint_file(name){
  if (name.length > 20) {
    if(name.length > 24){
      var shortened_name = name.substring(0, 20);
      var tipo = name.substring(name.length - 3);
      return shortened_name+'...'+tipo;
    }else{
      var shortened_name = name.substring(0, 16);
      var tipo = name.substring(name.length - 3);
      return shortened_name+'...'+tipo;
    }
  }else{
    return name;
  }
}

export function get_file_fron_db(){
  //AJAX
  $.ajax({
      url: "/download_doc_path/",
      method: "GET",
      data:{
          'id_fut': fut_id,// ESTA VARIABLE ESTA DEFINIDA EN view_fut.html
      },
      success: function(response){
          const midata = response;
          console.log(midata);
          pop_up_download_file();
      },
      error: function() {
          alert("Ocurrió un error al cargar el contenido.");
      }
  });
}

// CREAMOS UN FORMULARIO POP-UP PARA DESCARGAR EL DOCUMENTO
function pop_up_download_file(){
  let num_id = fut_id;// fut_id DE DELARO EN view_fut
  var alert_down_html = `
    <form action="/direct_download_path/" method="get" accept-charset="utf-8">
      <div class="pop_up_window">
          <div onclick="close_pop_up()" class="close" style="right: 15px;">
            <svg viewBox="0 0 1024 1024" fill="currentColor" aria-hidden="false" focusable="false"><path d="M181.088 135.936l1.536 1.44L512 466.741333l329.376-329.365333a32 32 0 0 1 46.688 43.712l-1.44 1.536L557.258667 512l329.365333 329.376a32 32 0 0 1-43.712 46.688l-1.536-1.44L512 557.258667 182.624 886.624a32 32 0 0 1-46.688-43.712l1.44-1.536L466.741333 512 137.376 182.624a32 32 0 0 1 43.712-46.688z"></path></svg>
          </div>
          <div class="report_content">
              <h3>DOCUMENTO EMITIDO POR SECRETARIA</h3>
              <label><strong>TIPO DE ARCHIVO:</strong> .pdf</label>
              <label><strong>N° DE FOLIOS:</strong> 5</label>
              <label><strong>DETALLES DE IMPRESION:</strong> El documento se tiene de imprimir en una papel bon A4 y entregarsele la alumno</label>

              <input type="hidden" name="fut_id" value="${num_id}">
              <button>Descargar</button>
          </div>
      </div>
    </form>
  `;
  var cont_pop = document.getElementById("pop_windows_report");
  cont_pop.classList.remove("ocultar");
  cont_pop.innerHTML = alert_down_html;
}