export function create_pop_notifi(){
  var noti_html = `
    <img src="/static/img/bell.png" alt="">
        <!-- - -->
        <div id="id_desplegable_notification" class="desplegable_content">
          <div class="nav_desp">
              <div class="lado">
              Notificaciones
              </div>
              <div class="lado">
                <img class="closeImg" src="/static/img/close2.png">
              </div>
          </div>
          <div id="content_not_princip2" class="content_Desp">
              <div class="empty_desp">
              <p>Aqui no hay Nada.</p>
              </div>
          </div>
        </div>
  `;

  cont_general_moti.innerHTML = noti_html;
  insertNotificaction("/get_notification_path/", "notification");
}

export function insertNotificaction(url_view, area){
  //AJAX
  console.log(url_view);
  $.ajax({
      url: url_view, // ruta en url.py para que ejecute una funcion
      method: "GET",
      success: function(response){
          const midata = response; //en response esta recibiendo el return de la funcion

          if(midata['data'] == null || midata['data']['length'] == 0){
            console.log("NO HAY NOTIFICACIONES");
          }else{
            console.log("SI HAY NOTIFICACIONES");
            if(area == "ticket"){
              paint_noti(midata);
            }else{
              paint_noti_2(midata);
            }
          }
      },
      error: function() {
          alert("Ocurrió un error al cargar el contenido.");
      }
  });
}



function paint_noti(midata){
  document.getElementById("content_not_princip").innerHTML = "";
  for (var i = 0; i < midata['data']['length']; i++) {

    console.log("CALCULAMOS DATE");
    let date = calcularTiempoTranscurrido(midata['data'][i]['date']);

    let pendiente = "";
    if(midata['data'][i]['view'] == false){
      pendiente = "style='background:#E8F5FD;'";
    }else{
      pendiente = "";
    }
    var notis = `
      <div onclick="openfut(${midata['data'][i]['fut_id_id']})" class="desplegable" ${pendiente}>
              <div class="lado">
                <div class="punto"></div>
                <div class="arreglo">
            <img src="/static/img/message_noti.png" alt="">
                </div>
                <div class="arreglo colum">
            <p><strong>${midata['data'][i]['tittle']}</strong></p>
                  <p style="opacity: 60%">${date}</p>
                </div>
              </div>
              <div class="lado colum">
              <p>${midata['data'][i]['charge']}</p>
              </div>
          </div>
    `;
      document.getElementById("content_not_princip").innerHTML += notis;
  }

}

function paint_noti_2(midata){
  document.getElementById("content_not_princip2").innerHTML = "";
  for (var i = 0; i < midata['data']['length']; i++) {

    let date = calcularTiempoTranscurrido(midata['data'][i]['date']);
    let pendiente = "";
    if(midata['data'][i]['view'] == false){
      pendiente = "style='background:#CCE4F3;'";
    }else{
      pendiente = "";
    }
    var notis = `
      <div onclick="openfut(${midata['data'][i]['fut_id_id']})" class="desplegable" ${pendiente}>
              <div class="lado">
                <div class="punto"></div>
                <div class="arreglo">
            <img src="/static/img/tramite_noti.png" alt="">
                </div>
                <div class="arreglo colum">
            <p><strong>${midata['data'][i]['tipo']}</strong></p>
                  <p style="opacity: 60%">${date}</p>
                </div>
              </div>
              <div class="lado colum">
              <p>${midata['data'][i]['emitido']}</p>
              </div>
          </div>
    `;
      document.getElementById("content_not_princip2").innerHTML += notis;
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