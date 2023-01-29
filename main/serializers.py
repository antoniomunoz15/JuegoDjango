from django.db import models
from rest_framework import serializers
from main.models import Vehiculo

# class VehiculoSerializer1(serializers.Serializer):
#     TIPOS = [
#         ('Coche', 'Coche'),
#         ('Ciclomotor', 'Ciclomotor'),
#         ('Motocicleta', 'Motocicleta'),
#     ]
#
#     MARCAS = [
#         ('Renault', 'Renault'),
#         ('Seat', 'Seat'),
#         ('BMW', 'BMW'),
#     ]
#
#     COLORES = [
#         ('Negro', 'Negro'),
#         ('Rojo', 'Rojo'),
#         ('Gris', 'Gris'),
#         ('Azul', 'Azul'),
#
#     ]
#     matricula = serializers.CharField(max_length=30, read_only=True)
#     tipo = serializers.CharField(max_length=11, choices=TIPOS, default='Coche')
#     chasis = serializers.IntegerField(unique=True)
#     marca = serializers.CharField(max_length=30, choices=MARCAS, default='BMW')
#     modelo = serializers.CharField(max_length=40)
#     color = serializers.CharField(max_length=30, choices=COLORES, default='Negro')
#     fecha_fabrica = serializers.DateField()
#     fecha_matricula = serializers.DateField(null=True, blank=True)
#     fecha_baja = serializers.DateField(allow_null=True, allow_blank=True)
#     suspendido = serializers.BooleanField(default=False)
#
#     def create(self, validated_data):
#         return Vehiculo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.matricula = validated_data.get('matricula', instance.matricula)
#         instance.tipo = validated_data.get('tipo', instance.tipo)
#         instance.chasis = validated_data.get('chasis', instance.chasis)
#         instance.marca = validated_data.get('marca', instance.marca)
#         instance.modelo = validated_data.get('modelo', instance.modelo)
#         instance.color = validated_data.get('color', instance.color)
#         instance.fecha_fabrica = validated_data.get('fecha_fabrica', instance.fecha_fabrica)
#         instance.fecha_matricula = validated_data.get('fecha_matricula', instance.fecha_matricula)
#         instance.fecha_baja = validated_data.get('fecha_baja', instance.fecha_baja)
#         instance.suspendido = validated_data.get('marca', instance.suspendido)
#         instance.save()
#         return instance

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['matricula', 'tipo', 'chasis', 'marca', 'modelo', 'color', 'fecha_fabrica', 'fecha_matricula', 'fecha_baja', 'suspendido']