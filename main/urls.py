from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from main.views import *

router = DefaultRouter()
router.register(r'frase', FraseViewSet, basename='frase')
router.register(r'usuario', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
