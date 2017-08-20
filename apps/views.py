from django.shortcuts import render
from apps.producto.models import Producto
from apps.forms import ContactoForm
from apps.ygoapp.models import Usuario
from django.core.mail import send_mail

def home(request):
    data = Producto.objects.all().order_by('-fecha_salida')[:4]
    return render(request,'landing/landing.html',{'data': data})

def timeline(request):
    return render(request,'landing/timeline.html',{})

def howToPlay(request):
    return render(request,'landing/comoSeJuega.html',{})

def estadisticas(request):
    return render(request,'landing/estadisticas.html',{})

def contactenos(request):
    if request.method == "POST":
        motivo = request.POST.get('Motivo')
        descripcion = request.POST.get('Descripcion')
        administrador = Usuario.objects.get(rol = 'administrador')
        admin_user = administrador.usuario.email
        print(admin_user)
        send_mail(
            motivo,
            descripcion,
            'alex.man.005x@gmail.com',
            [admin_user],
            fail_silently=False,
        )
        form = ContactoForm()
        return render(request, 'landing/contactenos.html',{'form': form})
    else:
        form = ContactoForm()
        return render(request, 'landing/contactenos.html',{'form': form})
    
