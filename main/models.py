from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Vehiculo(models.Model):
    TIPOS = [
        ('Coche', 'Coche'),
        ('Ciclomotor', 'Ciclomotor'),
        ('Motocicleta', 'Motocicleta'),
    ]

    MARCAS = [
        ('Renault', 'Renault'),
        ('Seat', 'Seat'),
        ('BMW', 'BMW'),
    ]

    COLORES = [
        ('Negro', 'Negro'),
        ('Rojo', 'Rojo'),
        ('Gris', 'Gris'),
        ('Azul', 'Azul'),

    ]
    matricula = models.CharField(primary_key=True, max_length=30)
    tipo = models.CharField(max_length=11, choices=TIPOS, default='Coche')
    chasis = models.PositiveIntegerField(unique=True)
    marca = models.CharField(max_length=30, choices=MARCAS, default='BMW')
    modelo = models.CharField(max_length=40)
    color = models.CharField(max_length=30, choices=COLORES, default='Negro')
    fecha_fabrica = models.DateField()
    fecha_matricula = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    suspendido = models.BooleanField(default=False)

    def __str__(self):
        return self.matricula + ": " + self.marca + ", " + self.modelo + ", " + self.color

class Patinete(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    precio_desbloque = models.FloatField([MinValueValidator(0.1)])
    precio_minuto = models.FloatField([MinValueValidator(0.1)])

    def __str__(self):
        return self.numero + ", " + self.tipo

class Alquiler(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.RESTRICT)
    patinete = models.ForeignKey(Patinete, on_delete=models.RESTRICT)
    fecha_desbloqueo = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    coste_final = models.FloatField(validators=[MinValueValidator(0.1)])

class Usuario(models.Model):
    debito = models.FloatField(validators=[MinValueValidator(0.1)], default=0)