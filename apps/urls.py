from django.conf.urls import include, url

from apps.views import home

urlpatterns = [
    url(r'', home),
]
