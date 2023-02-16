from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.db.models import Q, Count
from rest_framework import viewsets, permissions, status, mixins, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from main.models import *
from main.serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FraseViewSet(viewsets.ModelViewSet):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer
