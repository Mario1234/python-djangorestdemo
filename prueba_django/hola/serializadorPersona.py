from rest_framework import serializers
from .models import Persona


class SerializadorPersona(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    fecha_nacimiento = serializers.DateField()
    dni_sin_letra = serializers.IntegerField()
    sexo = serializers.ChoiceField(choices=Persona.SEXOS)

    def create(self, datos_validados):
        return Persona.objects.create(**datos_validados)

    def update(self, instancia, datos_validados):
        instancia.nombre = datos_validados.get('nombre', instancia.nombre)
        instancia.fecha_nacimiento = datos_validados.get('fecha_nacimiento', instancia.fecha_nacimiento)
        instancia.dni_sin_letra = datos_validados.get('dni_sin_letra', instancia.dni_sin_letra)
        instancia.sexo = datos_validados.get('sexo', instancia.sexo)
        instancia.save()
        return instancia