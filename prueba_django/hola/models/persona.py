from django.db import models


class Persona(models.Model):

    HOMBRE = 'Hombre'
    MUJER = 'Mujer'

    SEXOS = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer')
    )

    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni_sin_letra = models.IntegerField(default=12345678)
    sexo = models.CharField(max_length=10, choices=SEXOS)