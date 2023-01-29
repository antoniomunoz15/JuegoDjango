from django.db import models

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