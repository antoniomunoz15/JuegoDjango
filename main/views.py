from datetime import datetime, timezone

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from main.models import Vehiculo, Marca
from main.serializers import VehiculoSerializer, MarcaSerializer
from rest_framework import viewsets, permissions, status

from django_filters.rest_framework import *
from rest_framework import viewsets, permissions, filters
from main.serializers import *


# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

    #filtrado por marca, color y modelo ordenados por fecha de fabricación
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['fecha_fabrica']
    filterset_fields = ['marca', 'color', 'modelo']

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

#sólo editores pueden editar:
#en permissions.py:
# class IsEditorOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.groups.filter(name='Editores') or request.method in SAFE_METHODS:
#             return True
#         return False
#


#------------------------------------------------------------------------------------------------------------------EJ2:
class PatineteViewSet(viewsets.ModelViewSet):
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]

    @action(detail=True)
    def alquilar(self, request, pk=None):
        patinete = get_object_or_404(Patinete, numero=pk)
        alquiler = Alquiler.objects.all().filter(patinete=patinete).order_by('fecha_desbloqueo').last()

        if (alquiler is not None and alquiler.fecha_entrega) or (alquiler is None):
                usuario = get_object_or_404(Usuario, usuario=request.user)
                alquiler = Alquiler(usuario=usuario, patinete=patinete, fecha_desbloqueo=datetime.today())
                alquiler.save()
        else:
            usuario = get_object_or_404(Usuario, usuario=request.user)
            alquiler = Alquiler(usuario = usuario, patinete = patinete, fecha_desbloqueo = datetime.today())
            alquiler.save()
            print('Alquilando')

        serializador = self.get_serializer(patinete)
        return Response(serializador.data, status=status.HTTP_200_OK)


    @action(detail=True)
    def liberar(self, request, pk=None):
        patinete = get_object_or_404(Patinete, numero=pk)
        alquiler = Alquiler.objects.all().filter(patinete=patinete).order_by('fecha_desbloqueo').last()

        if alquiler and alquiler.fecha_entrega is None:
            diferencia_minutos = (datetime.now(timezone.utc) - alquiler.fecha_desbloqueo).total_seconds() / 60.0

            alquiler.fecha_entrega = datetime.today()
            alquiler.coste_final = patinete.precio_desbloque + (patinete.precio_minuto * diferencia_minutos)
            alquiler.save()
            print("Liberando")
        else:
            print("El patinete no está alquilado ahora mismo")

        serializador = self.get_serializer(patinete)
        return Response(serializador.data, status=status.HTTP_200_OK)

class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    permission_classes = [permissions.IsAdministrador]

#solo el administrador puede ver los alquileres
#en permissions.py:
# class IsAdministrador(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_superuser:
#             return True
#         return False

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsEditorOrReadOnly]