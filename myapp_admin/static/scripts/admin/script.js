//BOTÓN BOSPONER
function postponed(){
    var variable = 'Edgar';
    $.get('/viewsend/', {'id': fut_id, 'stage': 1}); // fut_id LA DECLARAMOS EN view_fut.html
    
    //redireccionamos a la pagina anterior
    setTimeout(function() {
        location.replace("/ils_admin/staff_treasury");
        console.log("fernan crack");
        //location.reload(true);
    }, 100);
}
//BOTÓN PENDIENTE
function pending(){
    var variable = 'Edgar';
    $.get('/viewsend/', {'id': '{{objs.id}}', 'stage': 2});

    //redireccionamos a la pagina anterior
    setTimeout(function() {
        location.replace("/ils_admin/staff_treasury");
    }, 100);
}

function open_pop_report(){
    adminsReporte();
    console.log("SE REPORTO");
    document.getElementById("pop_windows_report").classList.remove("ocultar");
    document.getElementById("id_report_content").classList.remove("ocultar");
}

// import { saludar } from './script_procesos.js';
// saludar("pedro");


// MOSTRAR EL POP-UP DE ENVIAR FUT
function send_fut(){
    //document.getElementById("login-form-popup").style.display = "block";
    document.getElementById("id_send_baucher").classList.remove("ocultar");
    document.getElementById("pop_windows_report").classList.remove("ocultar");
}
function issued_document(){
    // document.getElementById("cuestion_inssued2").style.display = "block"
    document.getElementById("id_publuc_direction").classList.remove("ocultar");
    document.getElementById("pop_windows_report").classList.remove("ocultar");
}
function process_secretary(){
    document.getElementById("id_procces_secretary").classList.remove("ocultar");
    document.getElementById("pop_windows_report").classList.remove("ocultar");
}
function clesed(){
    document.getElementById("login-form-popup").style.display = "none";
    document.getElementById("cuestion_send").style.display = "none";
    document.getElementById("inssued").style.display = "none";
    document.getElementById("cuestion_inssued").style.display = "none";
}
function cuestion_send(){
    // obtenemos el numero deboleta
   var ticket = document.getElementById('ticket');
   var text_ticket = ticket.value;

   // preguntamos
   var text_p = document.getElementById('text_p');
   text_p.innerHTML = '¿Estas seguro de que el codigo de boleta es:'+text_ticket+'?'

    document.getElementById("login-form-popup").style.display = "none";
    document.getElementById("cuestion_send").style.display = "block";
}
function yes_send(){
    // obtenemos el numero deboleta
    var ticket = document.getElementById('ticket');
    var text_ticket = ticket.value;
    console.log("jelouda, el tiked es:"+ text_ticket);

    $.get('/send_01/', {'ticket': text_ticket, 'id': '{{objs.id}}'});
    // redireccionamos a la pagina anterior
    setTimeout(function() {
        location.replace("/ils_admin/staff_treasury");
    }, 100);
}
function create_certificate(){
    document.getElementById("cuestion_inssued").style.display = "block"
    console.log('emitimos el certificado')
}
// PARA EMITIR EL CERTIFICADO
function issued_certificate(){
    document.getElementById("cuestion_inssued").style.display = "block"
    console.log('emitimos el certificado')
}

function cuestion_send_inssued(){
    console.log("CONFIRMAMOS LA EMISION DEL SERTIFICADO")
    document.getElementById("cuestion_inssued").style.display = "none"
    document.getElementById("inssued").style.display = "block"
}
// PARA DESCARGAR EL DOCUMENTO O CERTIFICADO
// function direction_download(){
//     console.log("Descargando");

//     $.get('/download/', {'id': '{{objs.id}}'});
    
// }

//VARIABLES DE VIEW FUTs
var id_cont_fut = document.getElementById("id_cont_fut");
var desplegable_hiden = document.getElementById("desplegable_hiden");
var desplegable_show = document.getElementById("desplegable_show");
var id_delhiden = document.getElementById("id_delhiden");
var id_colorFuncion = document.getElementById("id_colorFuncion");
//VARIABLES DE VIEW PAY
var id_cont_pay = document.getElementById("id_cont_pay");
var id_colorFuncion2 = document.getElementById("id_colorFuncion2");
var desplegable_show2 = document.getElementById("desplegable_show2");
var desplegable_hiden_2 = document.getElementById("desplegable_hiden_2");
var id_delhiden2 = document.getElementById("id_delhiden2");

function Show_FUTs(){
    id_cont_fut.classList.remove("fut_cont_A");
    id_cont_fut.classList.add("fut_cont_B");
    //DESPLEGABLES
    desplegable_show.classList.add("ocultar");
    desplegable_hiden.classList.remove("ocultar");
    //REPARACION DEL HIDEN
    id_delhiden.classList.add("fut_cont_B")
    //QUITAMOS EL COLOR_CONT  OCULTO Y QUITAMOS EL LLAMADO A LA FUNCIÓN
    id_colorFuncion.classList.add("ocultar");
}
function Hiden_FUTs(){
    id_cont_fut.classList.add("fut_cont_A");
    id_cont_fut.classList.remove("fut_cont_B");
    //DESPLEGABLES
    desplegable_show.classList.remove("ocultar");
    desplegable_hiden.classList.add("ocultar");
    //REPARACION DEL HIDEN
    id_delhiden.classList.remove("fut_cont_B")
    //AGREGAMOS EL COLOR_CONT  OCULTO Y AGREGAMOS EL LLAMADO A LA FUNCIÓN
    id_colorFuncion.classList.remove("ocultar");
}
//PAY FUNCTIONS
function Show_PAY(){
    id_cont_pay.classList.remove("fut_cont_A");
    id_cont_pay.classList.add("fut_cont_B");
    //DESPLEGABLES
    desplegable_show2.classList.add("ocultar");
    desplegable_hiden_2.classList.remove("ocultar");
    //REPARACION DEL HIDEN
    id_delhiden2.classList.add("fut_cont_B");
    //QUITAMOS EL COLOR_CONT  OCULTO Y QUITAMOS EL LLAMADO A LA FUNCIÓN
    id_colorFuncion2.classList.add("ocultar");

    process_show_img();
}
function Hiden_PAY(){
    id_cont_pay.classList.add("fut_cont_A");
    id_cont_pay.classList.remove("fut_cont_B");
    //DESPLEGABLES
    desplegable_show2.classList.remove("ocultar");
    desplegable_hiden_2.classList.add("ocultar");
    //REPARACION DEL HIDEN
    id_delhiden2.classList.remove("fut_cont_B");
    //QUITAMOS EL COLOR_CONT  OCULTO Y QUITAMOS EL LLAMADO A LA FUNCIÓN
    id_colorFuncion2.classList.remove("ocultar");
}
var id_cont_ticket = document.getElementById("id_cont_ticket");
function get_and_create_img(){
    return new Promise(function (resolve, reject){
        //AJAX
        $.ajax({
            url: "/obtain_img/",
            method: "GET",
            data:{
                'fut_id': fut_id,// Esta variable fue declarada en view_fut.html
            },
            success: function(response){
                const midata = response;
                resolve(midata)
            },
            error: function() {
                alert("Ocurrió un error al cargar el contenido.");
            }
        });
    });
}

function paint_img(){
    document.getElementById("img_pay_cont").innerHTML = `<img onclick="img_big()" class="img_pay" src="/static/tmp/pay_photo_${fut_id}.jpg" alt="">`;
}

async function process_show_img(){
    // OBTENEMOS LA IMG DE PAGO Y LA ESCRIBIMOS EN LA CARPETA tmp
    await get_and_create_img();
    // AGREGAMOS LA ETIQUTA IMG CON EL CALL CORRESPONDIENTE
    paint_img();
}

function img_big(){
    document.getElementById("id_cont_img_pop").innerHTML = `<img src="/static/tmp/pay_photo_${fut_id}.jpg" alt="">`;
    document.getElementById("pop_windows_report").classList.remove("ocultar");
    document.getElementById("id_pop_img").classList.remove("ocultar");
}


// ESTO ABRE OBSERVACIÓN Y CARGA EL NUMERO DE TIKET
function OpenTicket(){
    id_cont_ticket.classList.remove("ocultar");
    
    //SCROLL HACIA ABAJO
    const miElemento = document.getElementById('id_contFUT_p');
    miElemento.scrollTo({
        // top: 0, //Hace scroll hacia arriba
        top: miElemento.scrollHeight, // Hace scroll hacia abajo
        behavior: 'smooth'
    });
    //CREAMOS EL TICKET
    //CREAR_TICKET();
}
function DeletedTicket(){
    id_cont_ticket.classList.add("ocultar");
    //BORRAMOS EL CONTENIDO DE LOS TEXT
    document.getElementById("id_titulo").value="";
    document.getElementById("id_desarrollo").value="";
    eliminarCookie("id_ticket");
}

//FUNCIONES DE ABRIR UN TICKET------------
var pdf_file = document.getElementById("pdf_file");
var id_file_add_cont = document.getElementById("id_file_add_cont");
pdf_file.addEventListener('change', function(event){
    // Obtener la lista de archivos seleccionados
    var archivos = event.target.files;

    // Hacer algo con los archivos seleccionados
    for (var i = 0; i < archivos.length; i++) {
        console.log('Nombre del archivo:', archivos[i].name);
        console.log('Tipo de archivo:', archivos[i].type);
        console.log('Tamaño del archivo:', archivos[i].size, 'bytes');
        const name = archivos[i].name;
        const size = Math.floor(archivos[i].size / 1024);// CONVERTIMOS A cantidadKilobytes
        add_File(name, size);
    }
});

async function add_File(name, size){
    console.log("AQUI ESTAMOS");
    const id_generate = await generarStringAleatorio();
    id_file_add_cont.innerHTML += "<div id='"+id_generate+"' class='files_adjunts_cont'>"+
        "<div class='files_adjunts loadd'>"+
        "<img src='/static/img/adjunt_icon.png' alt=''>"+
        "<p>"+name+"</p>"+
        "<p style='color:#BFBFBF;'>("+size+" K)</p>"+
        "<div class='loader-spinner'></div>"+
        "</div>"+
        "</div>";

    //SCROLL HACIA ABAJO
    const miElemento = document.getElementById('id_contFUT_p');
    miElemento.scrollTo({
        // top: 0, //Hace scroll hacia arriba
        top: miElemento.scrollHeight, // Hace scroll hacia abajo
        behavior: 'smooth'
    });

    await new Promise(resolve => setTimeout(resolve, 3000)); // 10000 milisegundos = 10 segundos
    document.getElementById(id_generate).innerHTML = "<div class='files_adjunts'>"+
        "<img src='/static/img/adjunt_icon.png' alt=''>"+
        "<p>"+name+"</p>"+
        "<p style='color:#BFBFBF;'>("+size+" K)</p>"+
        "</div>";
    console.log(id_generate);
}
async function generarStringAleatorio() {
    const caracteres = 'abcdefghijklmnopqrstuvwxyz';
    let resultado = '';
    for (let i = 0; i < 5; i++) {
        const indiceAleatorio = Math.floor(Math.random() * caracteres.length);
        resultado += caracteres.charAt(indiceAleatorio);
    }
    return resultado;
}

// OPEN CONTENT TICKET
async function ContOpen_Ticket(i, ticket_id){
    document.getElementById("idFront_ticket_"+i).classList.add("ocultar");
    console.log("OPEN: "+i);
    console.log("ID: "+ticket_id);
    let my_html = (`
        <div id="idBody_ticket_${i}" class="body_ticket open_tick">
            <div class="ticket_navbar" onclick="ContClose_Ticket(${i})">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true">
                    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z" fill="white"></path>
                </svg>
                <p>El pago fue realizado incorrectamente poporop</p>
                <p style="opacity: 70%;margin: auto 10px auto auto;">N°78924</p>
            </div>
            <!-- ----USER BAR--- -->
            <div id="space_answer_${i}">
                <!-- ----space_answer--- -->
            </div>
            <button id="btn_answer"><img src="/static/img/reply_red.png" alt="">Responder</button>
        </div>
    `);

    document.getElementById("id_aqui_desplegable_content_"+i).innerHTML = my_html;
    await add_answers(i, ticket_id);

    //SCROLL HACIA ABAJO
    const miElemento = document.getElementById('id_contFUT_p');
    miElemento.scrollTo({
        // top: 0, //Hace scroll hacia arriba
        top: miElemento.scrollHeight, // Hace scroll hacia abajo
        behavior: 'smooth'
    });
}

function verificarArchivoExistente(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', url, false);
    xhr.send();

    return xhr.status === 200;
}

async function add_answers(num_for, id_ticket){
    console.log("ESTAMOS EN ANSWER_");
    var data_tickets = await all_data_desarrollo(id_ticket);
    // VARIABLES
    let length = data_tickets['more_tickets']['length'];

    for (let i = 0; i < length; i++) {
        // VARIABLES
        let id = data_tickets['more_tickets'][i]['id'];
        let titulo = data_tickets['more_tickets'][i]['name'];
        let desarrollo = data_tickets['more_tickets'][i]['desarrollo'];
        let charge = data_tickets['more_tickets'][i]['charge'];
        let date = data_tickets['more_tickets'][i]['date'];

        let existencia_url = verificarArchivoExistente(`/static/tmp/desarrollo_attach_${id}.jpg`) ? `<img src="/static/tmp/desarrollo_attach_${id}.jpg">` : '';
        console.log(existencia_url);
        let content_answer = (`
            <div class="sapace_user">
                <div id="id_img_space_${i}" class="user_img">
                    <img src="/static/img/admin_icon.png" alt="">
                </div>
                <div class="user_datecontent">
                    <hr>
                    <div class="user_date">
                        <div class="ladoB">
                            <h4>${titulo}</h4>
                            <p>(${charge})</p>
                        </div>
                        <div class="ladoB" style="margin: auto 10px;">
                            <p>${date}</p>
                        </div>
                    </div>
                    <hr>
                    <!-- -----TICKET---- -->
                    <div class="cont_of_ticket">
                        <p>
                            ${desarrollo}
                        </p>
                        ${existencia_url}
                        <div class="attach">
                        </div>
                        <div id="sello_${i}">
                            <img src="/static/img/tesoreria_identification.jpg" alt="">
                        </div>
                    </div>
                </div>
            </div>
        `);
        document.getElementById("space_answer_"+num_for).innerHTML += content_answer;

        if(charge == "alumno"){
            document.getElementById("sello_"+i).innerHTML = ``;
            document.getElementById("id_img_space_"+i).innerHTML = `<img src="/static/img/profile_user_test.jpg" alt="">`;

        }else{
            document.getElementById("sello_"+i).innerHTML = `<img src="/static/img/tesoreria_identification.jpg" alt="">`;
        }
    }
}

function ContClose_Ticket(i){
    //MOSTRAMOS EL CONTENEDOR FRONT DEL TICKET
    document.getElementById("idFront_ticket_"+i).classList.remove("ocultar");
    //ELIMINAMOS EL DESPLEGABLE COMPLETAMENTE (para que luego con ContOpen_Ticket lo podamos volver a generar)
    document.getElementById("id_aqui_desplegable_content_"+i).innerHTML = "";
}

//FUNCIONES PARA ENVIAR EL TICKET------
function sendTicket(){
    //TICKET_ACTUALIZAR_DESARROLLO();
    console.log("Se canceló esto (borrar rastros de codigo)");
}

//TICKET FUNCTIONS ------------------
async function CREAR_TICKET(){
    const name_creator = nameAdmin;
    const charge = chargeAdmin;
    const num_ticket = await Ramdom_string();

    //APLICAR EL num_ticket A LA ETIQUETA p Y VALIDACÍON DE CREATE TICKET
    const id_num_ticket = document.getElementById("id_num_ticket").textContent;
    console.log(id_num_ticket);
    if(id_num_ticket == "..."){
        //CREAMOS EL TICKET EN LA BD
        document.getElementById("id_num_ticket").innerHTML = num_ticket;
        //AJAX
        $.ajax({
            url: "/create_ticket_path/", // ruta en url.py para que ejecute una funcion
            method: "GET",
            data:{
                'titulo':'null',// variable que se envia con el metodo get (opcional)
                'desarrollo': 'null',
                'creator': name_creator,
                'state': 'False',
                'charge': charge,
                'num_ticket': num_ticket,
                'admin_id': admin_id,
                'fut_id': fut_id,
                'user_id': user_id,
            },
            success: function(response){
                const midata = response; //en response esta recibiendo el return de la funcion

                //OBTENER EL NUMERO DE ID DEL TICKET CREADO Y LO  GUARDAMOS EN UNA COOKIE PARA USARLO EN DESARROLLO Y ATTACH(adjuntar pdf jpg)
                establecerCookie('id_ticket', midata['the_id_ticket']);
            },
            error: function() {
                alert("Ocurrió un error al cargar el contenido.");
            }
        });
    }else{
        //NO HACEMOS NADA
    }
}

async function TICKET_ACTUALIZAR_DESARROLLO(){
    const titulo = document.getElementById("id_titulo").value;
    const desarrollo = document.getElementById("id_desarrollo").value;
    const charge = "("+chargeAdmin+")";

    if(titulo !== "" && desarrollo !== "" && existeCookie('id_ticket')){ //ESTO VALIDA SI NO EXISTE LA COOKIE 'id_ticket'
        //ACTUALIZAMOS LA BD TIKET
        //HE INSERTAMOS UN DESARROLLO EN LA DB

        //AJAX
        $.ajax({
            url: "/update_desarrollo_path/", // ruta en url.py para que ejecute una funcion
            method: "GET",
            data:{
                'titulo':titulo,
                'desarrollo': desarrollo,
                'charge': charge,
                'ticket_id_db': obtenerValorCookie("id_ticket"), //SI EL IF PASO AQUI SIGNIFICA QUE EXISTE LA COOKIE (asi que obtenemos el valor de esa cookie)
                'name_admin': nameAdmin,// ESTA VARIABLE FUE DECLARADA EN view_fut.html
                'chargeAdmin': chargeAdmin,// ESTA VARIABLE FUE DECLARADA EN view_fut.html
                'fut_id': fut_id,// ESTA VARIABLE FUE DECLARADA EN view_fut.html
                'user_id': user_id,// ESTA VARIABLE FUE DECLARADA EN view_fut.html

            },
            success: function(response){
                const midata = response; //en response esta recibiendo el return de la funcion

                //TODO BIEN, ASI QUE BORRAMOS CONTENT TICKEET
                DeletedTicket();
                //TAMBIEN ACTUALIZAREMOS EL OTRO CONTENT PARA VISUALIZAR EL TICKET CREADO
                LOADING_TICKET();
            },
            error: function() {
                alert("Ocurrió un error al cargar el contenido.");
            }
        });
    }else{
        alert("Por favor rellene los campos requeridos. ")
    }
}
LOADING_TICKET();
function LOADING_TICKET(){
    console.log("Cargando tickets...");
    //AJAX
    $.ajax({
        url: "/loading_ticket_path/", // ruta en url.py para que ejecute una funcion
        method: "GET",
        data:{
            'id_fut':fut_id,
        },
        success: function(response){
            const midata_json = response; //en response esta recibiendo el return de la funcion
            
            show_cont_ticket(midata_json['num_registros'], midata_json);
        },
        error: function() {
            alert("Ocurrió un error al cargar el contenido.");
        }
    });
}
//la explicación esta en Apuuntes_Markdown
// function establecerCookie(nombre, valor) {
//     var fechaExpiracion = new Date();
//     fechaExpiracion.setDate(fechaExpiracion.getDate() + 1); // 1 día
//     var cookieString = nombre + "=" + valor + "; expires=" + fechaExpiracion.toUTCString() + "; path=/";
//     document.cookie = cookieString;
// }
function eliminarCookie(nombre) {
    var fechaExpiracion = new Date();
    fechaExpiracion.setFullYear(fechaExpiracion.getFullYear() - 1);
    var cookieString = nombre + "=; expires=" + fechaExpiracion.toUTCString() + "; path=/";
    document.cookie = cookieString;
}
function existeCookie(nombre) {
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
function obtenerValorCookie(nombre) {
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
async function show_more_ticket_date(id_ticket){
    await new Promise(resolve => setTimeout(resolve, 100)); // 10000 milisegundos = 10 segundos
    //OBTENER EL DESARROLLO DEL TICKET
    //AJAX
    return new Promise((resolve, reject) => {
        // OBTENER EL DESARROLLO DEL TICKET
        // AJAX
        $.ajax({
            url: "/more_loading_ticket_path/",
            method: "GET",
            data: {
                'id_ticket': id_ticket
            },
            success: function (response) {
                const midata_json = response;
                resolve(midata_json);

            },
            error: function () {
                reject("Ocurrió un error al cargar el contenido.");
            }
        });
    });
}

// OBTENER EL DESARROLLO DEL TICKET
async function all_data_desarrollo(id_ticket){
    await new Promise(resolve => setTimeout(resolve, 100)); // 10000 milisegundos = 10 segundos
    return new Promise((resolve, reject) => {
        // AJAX
        $.ajax({
            url: "/all_desarrollo_data_path/",
            method: "GET",
            data: {
                'id_ticket': id_ticket
            },
            success: function (response) {
                const midata_json = response;
                resolve(midata_json);
            },
            error: function () {
                reject("Ocurrió un error al cargar el contenido.");
            }
        });
    });
}

async function show_cont_ticket(num_registros, midata_json){
    if(num_registros == 0){
        //LITERALMENTE NO HACEMOS NADA
    }else{
        document.getElementById("cont_padre_tickets").classList.remove("ocultar");

        console.log(midata_json['tickets'][0]);

        //limpiamos
        document.getElementById("content_dinamic").innerHTML = "";

        for (let i = 0; i < num_registros; i++) {
            console.log("TICKET CREATED, ID = "+ midata_json['tickets'][i]['id']);
            let tittle = midata_json['tickets'][i]['tittle'];
            let name_creator = midata_json['tickets'][i]['name_creator'];
            let num_ticket = midata_json['tickets'][i]['num_ticket'];
            let admin_id = midata_json['tickets'][i]['admin_id_id'];
            let ticket_id = midata_json['tickets'][i]['id'];
            //VAMOS A CARGAR DATOS EXTRA
            const lista = await show_more_ticket_date(ticket_id);
            let desarrollo = lista[0];
            let date = lista[1];
            let charge = "";
            if(lista[2] == chargeAdmin){
                charge = "<p style='background: #8FBED2;' class='received'>Enviado</p>";
            }else{
                charge = "<p style='background: #7BE47B;' class='received'>Recibido</p>";
            }
            let my_html = `
            <div id="cont_dinamic2_${i}">
                <div id="idFront_ticket_${i}" onclick="ContOpen_Ticket(${i}, ${ticket_id})" class="body_ticket">
                    <div class="nivel">
                        <div class="lado">
                            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true">
                                <path class="st0" d="M5.3,3.1c0.3-0.3,0.8-0.3,1.1,0c0,0,0,0,0,0l4.3,4.2c0.3,0.3,0.3,0.8,0,1.1c0,0,0,0,0,0l-4.2,4.3  c-0.3,0.3-0.8,0.3-1.1,0s-0.3-0.8,0-1.1l3.7-3.7L5.3,4.2C5,3.9,5,3.4,5.3,3.1C5.3,3.1,5.3,3.1,5.3,3.1z" fill="white"></path>
                            </svg>
                            <p>${tittle}</p>
                            ${charge}
                            <p style="margin: auto 5px;">${desarrollo}...</p>
                        </div>
                        <div class="lado">
                            <p style="opacity: 80%;">N°${num_ticket}</p>
                        </div>
                    </div>
                    <div class="nivel">
                        <div class="lado">
                            <p>Creado Por</p>
                            <img src="/static/img/admin_icon.png" alt="">
                            <p><strong>Tesorera - ${name_creator}</strong></p>
                            <p style="margin: auto 5px; opacity: 80%;">${date}</p>
                        </div>
                    </div>
                </div>
                <div id="id_aqui_desplegable_content_${i}"></div>
            </div>
            `;
            document.getElementById("content_dinamic").innerHTML += my_html;
        }
    }
}
async function Ramdom_string() {
    const caracteres = '123456789';
    let resultado = '';
    for (let i = 0; i < 5; i++) {
        const indiceAleatorio = Math.floor(Math.random() * caracteres.length);
        resultado += caracteres.charAt(indiceAleatorio);
    }
    return 88888;
}

// REPORT
if(report_state == 'True'){
    console.log("jajaja");
    stateReport();
}

function Ajax_consult(url, data){
    //url EXAPMLE: "/procedures_list/"
    $.ajax({
        url: url, // ruta en url.py para que ejecute una funcion
        method: "GET",
        // data:{
        //     'var':'var_txt',
        // },
        data: data,
        success: function(response){
            const midata = response; //en response esta recibiendo el return de la funcion
            dataReport(midata);
        },
        error: function() {
            alert("Ocurrió un error al cargar el contenido de reporte error Forky346.");
        }
    });
}

function stateReport(){
    var data = {
        id_fut: fut_id //fut_id esta declarado en el html
    };
    Ajax_consult('/select_report_path/', data);
}

function dataReport(midata){
    console.log(midata);
    let = message = midata['menssage'];
    let = description = midata['description'];
    let html_report = `
    <div class="title_cont">
        <p class="report_tittle"><strong>Este FUT fue reportado por: </strong></p>
        <p class="report_tittle">Nov. 22, 2023</p>
    </div>
    <hr>
    <p class="report_p"><strong>${message}</strong></p>
    <p class="report_p">${description}</p>
    `;
    document.getElementById("contid_report").innerHTML = html_report;
}
function download_final(){
    console.log("PAPADA_2");
    $.ajax({
        url: "/direct_download_path/",
        method: "GET",
        data:{
            'id_fut': fut_id,// ESTA VARIABLE ESTA DEFINIDA EN view_fut.html
        },
        success: function(response){
            const midata = response;
            console.log(midata);
        },
        error: function() {
            alert("Ocurrió un error al cargar el contenido.");
        }
    });
}