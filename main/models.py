from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
class Marca(models.Model):
    nombre_marca = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_marca
class Vehiculo(models.Model):
    TIPOS = [
        ('Coche', 'Coche'),
        ('Ciclomotor', 'Ciclomotor'),
        ('Motocicleta', 'Motocicleta'),
    ]

    COLORES = [
        ('Negro', 'Negro'),
        ('Rojo', 'Rojo'),
        ('Gris', 'Gris'),
        ('Azul', 'Azul'),

    ]
    matricula = models.CharField(unique=True, max_length=30)
    tipo = models.CharField(max_length=11, choices=TIPOS, default='Coche')
    chasis = models.CharField(primary_key=True, unique=True, max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=40)
    color = models.CharField(max_length=30, choices=COLORES, default='Negro')
    fecha_fabrica = models.DateField()
    fecha_matricula = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    suspendido = models.BooleanField(default=False)

    def __str__(self):
        return self.matricula + ": " + self.modelo + ", " + self.color


#-------------------------------------------------------------------------------------------------------------------EJ2:

#EJ2:
class Patinete(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    precio_desbloque = models.FloatField()
    precio_minuto = models.FloatField()

    def __str__(self):
        return str(self.numero)

class Alquiler(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.RESTRICT)
    patinete = models.ForeignKey(Patinete, on_delete=models.RESTRICT)
    fecha_desbloqueo = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    coste_final = models.FloatField(validators=[MinValueValidator(0.1)], null=True, blank=True)
    def __str__(self):
        return str(self.patinete_id) + ", con fecha de dsbloqueo" + str(self.fecha_desbloqueo)

class Usuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    debito = models.FloatField(validators=[MinValueValidator(0.1)], default=0)
    def __str__(self):
        return str(self.usuario)