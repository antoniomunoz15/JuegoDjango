from django.conf import settings
from django.db import models

# Create your models here.
from django.contrib import auth
from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Frase(models.Model):
    frase = models.CharField(max_length=60)
    pista_inicial = models.CharField(max_length=60)

class Usuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    puntuacion = models.PositiveIntegerField(null=True, blank=True)
    puntos_iniciales = models.PositiveIntegerField(default=200)
    def __str__(self):
        return str(self.usuario)


