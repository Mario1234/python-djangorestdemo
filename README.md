# python-djangorestdemo
Servicio REST de ejemplo escrito en python con Django y djangorestframework


instalar Python 2.7.14

instalar pytz, django y djangorestframework, abre la consola de comandos en modo administrador y escribe:

python -m pip install pytz-2018.4.tar.gz

python -m pip install Django-1.11.12.tar.gz

python -m pip install djangorestframework-3.8.2.tar.gz


ir al escritorio:
cd desktop

si no quieres desarrollar esta app desde cero
saltar las siguientes instrucciones hasta *+*

	Crea un dominio django (prueba_django):
	django-admin.py startproject prueba_django	
	
	y una aplicacion web (hola):
	django-admin.py startapp hola	
	
	dentro de la carpeta recien creada prueba_django ir a subcarpeta prueba_django:	
	Escribir <'hola.apps.HolaConfig',> en el archivo settings.py
	Escribir <url(r'', include('hola.mapeador')),> en el archivo urls.py
	ir a la carpeta hola:
	copiar pegar mapeador.py
	la linea <url(r'^personas/$', views.lista_personas, name='inicio'),> define
	que para la ruta /personas/ se debe ejecutar el metodo lista_personas de la hoja de codigo views
	comprobar que el nombre de la clase del archivo apps.py es HolaConfig
	copiar pegar serializadorPersona.py
	ahi se define la transformacion entre objeto vista(en este caso JSON) y objeto modelo
	y tambien administra las validaciones
	copiar pegar views.py
	es el codigo del controllador web
	eliminar models.py
	crear carpeta models
	ir a carpeta models:
	crear __init__.py con los imports de todos nuestras tablas/modelos de la base de datos
	persona.py creara una tabla en la base de datos de django (esta en prueba_django se llama db.sqlite3)
	volver a la carpeta hola:
	ejecutar comandos de creacion de modelo Django:
	./manage.py makemigrations hola
	./manage.py migrate
	
*+*
ir a la carpeta prueba_django:

cd DjangoRest

cd prueba_django

./manage.py runserver


probar servicio rest en el navegador web:
http://localhost:8000/personas/
