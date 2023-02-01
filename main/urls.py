from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from main import views

router = DefaultRouter()
router.register(r'vehiculos', views.VehiculoViewSet,basename="vehiculo")
router.register(r'marcas', views.MarcaViewSet,basename="marca")
router.register(r'patinete', views.PatineteViewSet,basename="patinete")
router.register(r'alquiler', views.AlquilerViewSet,basename="alquiler")
router.register(r'usuario', views.UsuarioViewSet,basename="usuario")

urlpatterns = [
    path('admin/', admin.site.urls),
    #ruta para establecer idioma
    path('', include(router.urls)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', TemplateView.as_view(template_name='main/index.html'), name='welcome'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='main/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
