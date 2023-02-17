from rest_framework import serializers

from main.models import Frase, Usuario


class FraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frase
        fields = ['frase', 'pista_inicial','url']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario', 'puntuacion', 'puntos_iniciales', 'url']
