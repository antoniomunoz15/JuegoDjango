from django.db import models
from rest_framework import serializers
from main.models import Vehiculo, Marca, Alquiler, Patinete, Usuario


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['chasis', 'matricula', 'tipo', 'marca', 'modelo', 'color', 'fecha_fabrica', 'fecha_matricula', 'fecha_baja', 'suspendido', 'url']

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'url', 'nombre_marca']


#EJ2:
class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['numero', 'url', 'tipo', 'precio_desbloque', 'precio_minuto']

class AlquilerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alquiler
        fields = ['id', 'url', 'usuario', 'patinete', 'fecha_desbloqueo', 'fecha_entrega', 'coste_final']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'url', 'debito']