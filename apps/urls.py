from django.conf.urls import include, url

from apps.views import home, timeline, howToPlay, estadisticas,contactenos
from apps.producto.views import productos, crearProducto, ajax_get_producto
from apps.torneo.views import torneos, listarTorneosIndividuales, listarUnTorneoIndividual, editarTorneoIndividual, eliminarTorneoIndividual, crearTorneoIndividual
from apps.carta.views import crearCarta, listaCartas
from apps.ygoapp.views import crearUsuario
from apps.torneo_grupal.views import listarTorneosGrupales, listarUnTorneoGrupal, editarTorneoGrupal, eliminarTorneoGrupal, crearTorneoGrupal

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
]
