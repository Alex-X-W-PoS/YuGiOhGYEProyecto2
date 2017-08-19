
$(document).ready(function(){
	console.log("ready");
	$(".btn").click(function(e) {

//Prevent default submit. Must for Ajax post.
 e.preventDefault();

//Prepare csrf token


 var tipo = this.id;


 $.ajax({
       url : "http://127.0.0.1:8000/productos/get/",
       type : "GET", 
       data : {
	   tipo : tipo,
 }, 


 success : function(json) {
	 console.log(json.length);
	 var cajon_contenido = document.getElementById("listado-seccion-productos");
	 var follow_box = document.getElementsByClassName("follow")[0];
	 let div_principal = document.createElement("div");
	 div_principal.setAttribute("class","container");
	 div_principal.setAttribute("id","listado-seccion-productos");
	 cajon_contenido.remove();
	 var longitud = json.length;
	 var cuerpo = document.getElementsByTagName("body")[0];	 
	 cuerpo.insertBefore(div_principal,follow_box);
	 if(json.length==0){
		 cuerpo.style.backgroundSize = "cover";
	 }
	 else{
		 cuerpo.style.backgroundSize = "contain";
		 div_principal.setAttribute("class","container content-box contenedor");
		 for (let i = 0; i<longitud;i++){
		 console.log(json[i].fields.nombre);
		 let div = document.createElement("div");
				div.setAttribute("class","product-listing");
				let div2 = document.createElement("div");
				div2.setAttribute("class","row");
				let div3 = document.createElement("div");
				div3.setAttribute("class","col-md-3 col-xs-3");
				let div4 = document.createElement("div");
				div4.setAttribute("class","col-md-6 col-xs-6");
				let div5 = document.createElement("div");
				div5.setAttribute("class","col-md-3 col-xs-3");
				let imagen = document.createElement("img");
				imagen.setAttribute("src",json[i].fields.url);
				imagen.setAttribute("alt",json[i].fields.codigo);
				imagen.setAttribute("class","product-image center-block");
				div3.appendChild(imagen);
				let p = document.createElement("p");
				p.setAttribute("class","product-title");
				let p1 = document.createElement("p");
				//p1.setAttribute("class","product-description");
				p.innerHTML = json[i].fields.nombre;
				//p1.innerHTML = array[i].descripcion;
				let br = document.createElement("br");
				div4.appendChild(p);
				div4.appendChild(br);
				//div4.appendChild(p1);
				let boton = document.createElement("button");
				boton.setAttribute("id",json[i].fields.codigo);
				boton.setAttribute("type","button");
				boton.setAttribute("class","btn btn-primary btn-block bouton-image monBouton");
				boton.innerHTML="<span>Lista de Cartas</span>";
				//if (i==0) {
				//	boton.onclick = function () { alert("Este sobre no ha salido en el país aún.\nLo actualizaremos cuando llegue.");};//esto debo cambiarlo luego :V
				//}
				//else {
				//	boton.onclick = function () { location.replace("https://alex-x-w-pos.github.io/ProyectoYuGiOhGYE/galeriaCartas/galeriaCartas" + i + ".html");};//esto debo cambiarlo luego :V
				//}
				div5.appendChild(boton);
				div2.appendChild(div3);
				div2.appendChild(div4);
				div2.appendChild(div5);
				div.appendChild(div2);
				div_principal.appendChild(div);
	 }
	 }
 //On success show the data posted to server as a message
 },


 error : function() {
 alert('Hubo un problema con el GET :C');
 }
 });
});
});

 

//});
