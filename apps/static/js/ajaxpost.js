

//For getting CSRF token
function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}



$(document).ready(function(){
	console.log("ready");
	$("#submit").click(function(e) {

//Prevent default submit. Must for Ajax post.
 e.preventDefault();

//Prepare csrf token
 var csrftoken = getCookie('csrftoken');



 var Motivo = $('#motive').val();
 var Descripcion = $('#descripcion').val();
 $.ajax({
       url : window.location.href,
       type : "POST", 
       data : { csrfmiddlewaretoken : csrftoken, 
       Motivo : Motivo,
       Descripcion : Descripcion
 }, 


 success : function() {
 //On success show the data posted to server as a message
 alert('Mensaje Enviado Exitosamente.');
 },


 error : function() {
 alert('Hubo un problema con el posting :C Asegúrese de llenar los campos obligatorios');
 }
 });
});
});

 

//});
