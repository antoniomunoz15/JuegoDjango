from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import Vehiculo
from main.serializers import VehiculoSerializer
# Create your views here.

@csrf_exempt
def listado_vehiculos(request):
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        serializador = VehiculoSerializer(vehiculos, many=True)
        return JsonResponse(serializador.data, safe=False)
    elif request.method == 'POST':
        datos = JSONParser().parse(request)
        serializador = VehiculoSerializer(data=datos)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data, status=201)
        return JsonResponse(serializador.errors, status=400)

@csrf_exempt
def detalle_vehiculo(request, matricula):
    try:
        vehiculo = Vehiculo.objects.get(matricula=matricula)
    except Vehiculo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehiculoSerializer(vehiculo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehiculo.delete()
        return HttpResponse(status=204)
