from django.conf.urls import include, url

from apps.views import home, timeline, howToPlay, estadisticas,contactenos, inscripcion
from apps.producto.views import productos, crearProducto, ajax_get_producto
from apps.torneo.views import torneos, listarTorneosIndividuales, listarUnTorneoIndividual, editarTorneoIndividual, eliminarTorneoIndividual, crearTorneoIndividual
from apps.carta.views import crearCarta, listaCartas
from apps.ygoapp.views import crearUsuario, mostrarPerfil,editarPerfil, verGrupos
from apps.torneo_grupal.views import listarTorneosGrupales, listarUnTorneoGrupal, editarTorneoGrupal, eliminarTorneoGrupal, crearTorneoGrupal
from apps.ficha_individual.views import crearFichaIndividual
from apps.ficha_grupal.views import crearFichaGrupal, ingresarFichaGrupal

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^productos$', productos, name = 'productos'),
    url(r'^torneos$', torneos, name = 'torneos'),
    url(r'^timeline$', timeline, name = 'timeline'),
    url(r'^howToPlay$', howToPlay, name = 'howToPlay'),
    url(r'^estadisticas$', estadisticas, name = 'estadisticas'),
    url(r'^contactenos$', contactenos, name ='contactenos'),
    url(r'^agregarProducto$',crearProducto, name = 'crearProducto'),
    url(r'^productos/get/', ajax_get_producto),
    url(r'^agregarCarta$',crearCarta, name = 'crearCarta'),
    url(r'^listaCartas/get/',listaCartas, name = 'listaCarta'),
    url(r'^agregarUsuario$',crearUsuario, name = 'crearUsuario'),
    url(r'^torneos_individuales/get/', listarTorneosIndividuales),
    url(r'^torneos_grupales/get/', listarTorneosGrupales),
    url(r'^torneoIndividualDetalles/get/',listarUnTorneoIndividual, name = 'listaUnTorneoIndividual'),
    url(r'^torneoIndividualEditar/(?P<id>\d+)$',editarTorneoIndividual, name = 'editar_torneo_individual'),
    url(r'^torneoIndividualEliminar/(?P<id>\d+)$',eliminarTorneoIndividual, name = 'eliminar_torneo_individual'),
    url(r'^torneoGrupalDetalles/get/',listarUnTorneoGrupal, name = 'listaUnTorneoGrupal'),
    url(r'^torneoGrupalEditar/(?P<id>\d+)$',editarTorneoGrupal, name = 'editar_torneo_grupal'),
    url(r'^torneoGrupalEliminar/(?P<id>\d+)$',eliminarTorneoGrupal, name = 'eliminar_torneo_grupal'),
    url(r'^torneoIndividualCrear$',crearTorneoIndividual, name = 'crearTorneoIndividual'),
    url(r'^torneoGrupalCrear$',crearTorneoGrupal, name = 'crearTorneoGrupal'),
    url(r'^registrarTorneoIndividual/(?P<id>\d+)$',crearFichaIndividual, name = 'ficha_torneo_individual'),
    url(r'^registrarTorneoGrupal/(?P<id>\d+)$',crearFichaGrupal, name = 'ficha_torneo_grupal'),
    url(r'^creacionFichaGrupal$',ingresarFichaGrupal, name = 'creacion_ficha_grupal'),
    url(r'^inscripcionExitosa$', inscripcion, name= 'inscripcionExitosa'),
    url(r'^mostrarPerfil$', mostrarPerfil, name='mostrarPerfil'),
    url(r'^editarPerfil$', editarPerfil, name='editarPerfil'),
    url(r'^verGrupos$', verGrupos, name='verGrupos'),
]
