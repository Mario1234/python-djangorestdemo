from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hola.models import Persona
from hola.serializadorPersona import SerializadorPersona
from datetime import datetime

class RespuestaJSON(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(RespuestaJSON, self).__init__(content, **kwargs)
		
@csrf_exempt
def lista_personas(peticion):
	if peticion.method == 'GET':
		fecnac1 = datetime.strptime('17-04-2011', '%d-%m-%Y').date()
		persona1 = Persona(nombre='Pedro', sexo='Hombre', fecha_nacimiento=fecnac1)
		persona1.save()
		fecnac2 = datetime.strptime('24-06-2015', '%d-%m-%Y').date()
		persona2 = Persona(nombre='Marta', sexo='Mujer', fecha_nacimiento=fecnac2)
		persona2.save()
		listaPersonas = Persona.objects.all()
		serializador = SerializadorPersona(listaPersonas, many=True)
		return RespuestaJSON(serializador.data)

	elif peticion.method == 'POST':
		datos = JSONParser().parse(peticion)
		serializador = SerializadorPersona(data=datos)
		if serializador.is_valid():
			serializador.save()
			return RespuestaJSON(serializador.data, status=201)
		return RespuestaJSON(serializador.errors, status=400)