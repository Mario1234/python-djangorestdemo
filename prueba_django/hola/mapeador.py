from django.conf.urls import url

from hola import views

urlpatterns = [
    url(r'^personas/$', views.lista_personas, name='inicio'),
]