from django.shortcuts import render, redirect
from apps.producto.models import Producto
from apps.forms import ContactoForm
from apps.ygoapp.models import Usuario
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from apps.jugador.models import Duelista

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                user_logged = request.user
                usuario_log = Usuario.objects.get(usuario = user_logged)
                username1 = user_logged.username
                if (usuario_log.rol=='jugador'):
                    duelista = Duelista.objects.get(usuario = usuario_log)
                    duelista.is_into_the_vrains = True
                    print(duelista.is_into_the_vrains)
                    duelista.save()
        #print(usuario_log.rol)
                request.session['rol'] = usuario_log.rol
                request.session['id'] = usuario_log.user_id
                print(request.session['id'])
            else:
                return render(request, 'landing/login.html')
        else:
            return render(request, 'landing/login.html')
    else:
        user_logged = request.user
        username1 = user_logged.username
        if user_logged.is_authenticated:
           data = Producto.objects.all().order_by('-fecha_salida')[:4]
           return render(request,'landing/landing2.html',{'data': data, 'username': username1})
        else:
            return render(request, 'landing/login.html')
    data = Producto.objects.all().order_by('-fecha_salida')[:4]
    return render(request,'landing/landing2.html',{'data': data, 'username': username1})

def logginOut(request):
    user_logged = request.user
    usuario_log = Usuario.objects.get(usuario = user_logged)
    if (usuario_log.rol=='jugador'):
        duelista = Duelista.objects.get(usuario = usuario_log)
        duelista.is_into_the_vrains = False
        print(duelista.is_into_the_vrains)
        duelista.save()
    logout(request)
    return redirect ('home')

def timeline(request):
    return render(request,'landing/timeline.html',{})

def inscripcion(request):
    return render(request,'landing/inscripcionExitosa.html',{})

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
            'yugiogye@gmail.com',
            [admin_user],
            fail_silently=False,
        )
        form = ContactoForm()
        return render(request, 'landing/contactenos.html',{'form': form})
    else:
        form = ContactoForm()
        return render(request, 'landing/contactenos.html',{'form': form})
    
