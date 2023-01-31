from django.db import models
from rest_framework import serializers
from main.models import Vehiculo, Marca


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['chasis', 'matricula', 'tipo', 'marca', 'modelo', 'color', 'fecha_fabrica', 'fecha_matricula', 'fecha_baja', 'suspendido', 'url']

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'url', 'nombre_marca']