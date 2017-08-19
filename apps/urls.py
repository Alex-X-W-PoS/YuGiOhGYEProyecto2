from django.conf.urls import include, url

from apps.views import home, timeline, howToPlay, estadisticas,contactenos
from apps.producto.views import productos, crearProducto, ajax_get_producto
from apps.torneo.views import torneos
from apps.carta.views import crearCarta

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
]
