from main.models import Vehiculo, Marca
from main.serializers import VehiculoSerializer, MarcaSerializer
from rest_framework import viewsets, permissions

from django_filters.rest_framework import *
from rest_framework import viewsets, permissions, filters
from main.serializers import *


# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['fecha_fabrica']
    filterset_fields = ['marca', 'color', 'modelo']

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

#EJ2:
class PatineteViewSet(viewsets.ModelViewSet):
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    permission_classes = [permissions.IsAdministrador]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]