
$(document).ready(function(){
	console.log("ready");
	$(".normal_button").click(function(e) {

//Prevent default submit. Must for Ajax post.
 e.preventDefault();

//Prepare csrf token


 var tipo = this.id;
 console.log(tipo);
	if (tipo.localeCompare("individual")==0){
		$.ajax({
       url : "http://127.0.0.1:8000/torneos_individuales/get/",
       type : "GET", 


 success : function(json) {
	 console.log(json.length);
	 var cajon_contenido = document.getElementById("listado-seccion-productos");
	 var follow_box = document.getElementsByClassName("follow")[0];
	 let div_principal = document.createElement("div");
	 let tabla = document.createElement("table");
	 div_principal.setAttribute("class","container contenedor");
	 div_principal.setAttribute("id","listado-seccion-productos");
	 cajon_contenido.remove();
	 var longitud = json.length;
	 var cuerpo = document.getElementsByTagName("body")[0];	 
	 cuerpo.insertBefore(div_principal,follow_box);
	 if(json.length==0){
		 cuerpo.style.backgroundSize = "cover";
	 }
	 else{
		 div_principal.appendChild(tabla);
		 let tableHead = document.createElement("thead");
		 let tr = document.createElement("tr");
		 let th1 = document.createElement("th");
		 let th2 = document.createElement("th");
		 let th3 = document.createElement("th");
		 let th4 = document.createElement("th");
		 let th5 = document.createElement("th");
		 let th6 = document.createElement("th");
		 th1.setAttribute("class","product-title");
		 th2.setAttribute("class","product-title");
		 th3.setAttribute("class","product-title");
		 th4.setAttribute("class","product-title");
		 th5.setAttribute("class","product-title");
		 th6.setAttribute("class","product-title");
		 th1.innerHTML="Nombre";
		 th2.innerHTML="Fecha y Hora Inicio";
		 th3.innerHTML="Fecha y Hora Fin";
		 th4.innerHTML="Espacios Disponibles";
		 th5.innerHTML="Ganador";
		 th6.innerHTML="Detalles";
		 tr.appendChild(th1);
		 tr.appendChild(th2);
		 tr.appendChild(th3);
		 tr.appendChild(th4);
		 tr.appendChild(th5);
		 tr.appendChild(th6);
		 tableHead.appendChild(tr);
		 tabla.appendChild(tableHead);
		 console.log(json);
		 cuerpo.style.backgroundSize = "contain";
		 for (let i = 0; i<longitud;i++){
			 let row = document.createElement("tr");
			 let td1 = document.createElement("td");
			 let td2 = document.createElement("td");
			 let td3 = document.createElement("td");
			 let td4 = document.createElement("td");
			 let td5 = document.createElement("td");
			 let td6 = document.createElement("td");
			 td1.setAttribute("class","product-description");
			 td2.setAttribute("class","product-description");
			 td3.setAttribute("class","product-description");
			 td4.setAttribute("class","product-description");
			 td5.setAttribute("class","product-description");
			 td6.setAttribute("class","product-description");
			 td1.innerHTML=json[i].fields.nombre;
			 let string1 = json[i].fields.fecha_hora_inicio;
			 let newstring1 = string1.replace("T","--");
			 let newstring2 = newstring1.replace("Z","");
			 td2.innerHTML=newstring2;
			 let string2 = json[i].fields.fecha_hora_fin;
			 let newstring3 = string2.replace("T","--");
			 let newstring4 = newstring3.replace("Z","");
			 td3.innerHTML=newstring4;
			 td4.innerHTML=json[i].fields.numero_participantes_disponibles;
			 td5.innerHTML=json[i].fields.ganador;
			 let boton = document.createElement("button");
				boton.setAttribute("id",json[i].pk);
				boton.setAttribute("type","button");
				boton.setAttribute("class","btn btn-primary btn-block especial");
				boton.innerHTML="<span>Ver</span>";
				//if (i==0) {
				//	boton.onclick = function () { alert("Este sobre no ha salido en el país aún.\nLo actualizaremos cuando llegue.");};//esto debo cambiarlo luego :V
				//}
				//else {
					boton.onclick = function (e) { 
					location.assign("http://127.0.0.1:8000/torneoIndividualDetalles/get/?identificacion=" + json[i].pk);  
					};//esto debo cambiarlo luego :V
				//}
			td6.appendChild(boton);
			row.appendChild(td1);	
			row.appendChild(td2);
			row.appendChild(td3);
			row.appendChild(td4);
			row.appendChild(td5);
			row.appendChild(td6);
			tabla.appendChild(row);
	 }
	 }
 //On success show the data posted to server as a message
 },


 error : function() {
 alert('Hubo un problema con el GET :C');
 }
 });
	}
	else{
		$.ajax({
       url : "http://127.0.0.1:8000/torneos_grupales/get/",
       type : "GET",  


  success : function(json) {
	 console.log(json.length);
	 var cajon_contenido = document.getElementById("listado-seccion-productos");
	 var follow_box = document.getElementsByClassName("follow")[0];
	 let div_principal = document.createElement("div");
	 let tabla = document.createElement("table");
	 div_principal.setAttribute("class","container contenedor");
	 div_principal.setAttribute("id","listado-seccion-productos");
	 cajon_contenido.remove();
	 var longitud = json.length;
	 var cuerpo = document.getElementsByTagName("body")[0];	 
	 cuerpo.insertBefore(div_principal,follow_box);
	 if(json.length==0){
		 cuerpo.style.backgroundSize = "cover";
	 }
	 else{
		 div_principal.appendChild(tabla);
		 let tableHead = document.createElement("thead");
		 let tr = document.createElement("tr");
		 let th1 = document.createElement("th");
		 let th2 = document.createElement("th");
		 let th3 = document.createElement("th");
		 let th4 = document.createElement("th");
		 let th5 = document.createElement("th");
		 let th6 = document.createElement("th");
		 th1.setAttribute("class","product-title");
		 th2.setAttribute("class","product-title");
		 th3.setAttribute("class","product-title");
		 th4.setAttribute("class","product-title");
		 th5.setAttribute("class","product-title");
		 th6.setAttribute("class","product-title");
		 th1.innerHTML="Nombre";
		 th2.innerHTML="Fecha y Hora Inicio";
		 th3.innerHTML="Fecha y Hora Fin";
		 th4.innerHTML="Espacios Disponibles";
		 th5.innerHTML="Grupo Ganador";
		 th6.innerHTML="Detalles";
		 tr.appendChild(th1);
		 tr.appendChild(th2);
		 tr.appendChild(th3);
		 tr.appendChild(th4);
		 tr.appendChild(th5);
		 tr.appendChild(th6);
		 tableHead.appendChild(tr);
		 tabla.appendChild(tableHead);
		 console.log(json);
		 cuerpo.style.backgroundSize = "contain";
		 for (let i = 0; i<longitud;i++){
			 let row = document.createElement("tr");
			 let td1 = document.createElement("td");
			 let td2 = document.createElement("td");
			 let td3 = document.createElement("td");
			 let td4 = document.createElement("td");
			 let td5 = document.createElement("td");
			 let td6 = document.createElement("td");
			 td1.setAttribute("class","product-description");
			 td2.setAttribute("class","product-description");
			 td3.setAttribute("class","product-description");
			 td4.setAttribute("class","product-description");
			 td5.setAttribute("class","product-description");
			 td6.setAttribute("class","product-description");
			 td1.innerHTML=json[i].fields.nombre;
			 let string1 = json[i].fields.fecha_hora_inicio;
			 let newstring1 = string1.replace("T","--");
			 let newstring2 = newstring1.replace("Z","");
			 td2.innerHTML=newstring2;
			 let string2 = json[i].fields.fecha_hora_fin;
			 let newstring3 = string2.replace("T","--");
			 let newstring4 = newstring3.replace("Z","");
			 td3.innerHTML=newstring4;
			 td4.innerHTML=json[i].fields.numero_participantes_disponibles;
			 td5.innerHTML=json[i].fields.grupo_ganador;
			 let boton = document.createElement("button");
				boton.setAttribute("id",json[i].pk);
				boton.setAttribute("type","button");
				boton.setAttribute("class","btn btn-primary btn-block especial");
				boton.innerHTML="<span>Ver</span>";
				//if (i==0) {
				//	boton.onclick = function () { alert("Este sobre no ha salido en el país aún.\nLo actualizaremos cuando llegue.");};//esto debo cambiarlo luego :V
				//}
				//else {
					boton.onclick = function (e) { 
					location.assign("http://127.0.0.1:8000/torneoGrupalDetalles/get/?identificacion=" + json[i].pk);  
					};//esto debo cambiarlo luego :V
				//}
			td6.appendChild(boton);
			row.appendChild(td1);	
			row.appendChild(td2);
			row.appendChild(td3);
			row.appendChild(td4);
			row.appendChild(td5);
			row.appendChild(td6);
			tabla.appendChild(row);
	 }
	 }
 //On success show the data posted to server as a message
 },


 error : function() {
 alert('Hubo un problema con el GET :C');
 }
 });
	}

 
});
});

 

//});
