from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register(r'vehiculos', views.VehiculoViewSet,basename="vehiculo")
router.register(r'marcas', views.MarcaViewSet,basename="marca")

urlpatterns = [
    path('admin/', admin.site.urls),
    #ruta para establecer idioma
    path('', include(router.urls)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', TemplateView.as_view(template_name='main/index.html'), name='welcome'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
