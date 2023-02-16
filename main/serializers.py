from rest_framework import serializers

from main.models import Frase, Usuario


class FraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frase
        fields = ['frase', 'url']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario', 'puntuacion', 'url']
