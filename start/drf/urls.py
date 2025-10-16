from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la documentación Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="API Clínica Salud Vital",
      default_version='v1',
      description="Documentación de la API para la gestión clínica - Sistema de gestión de pacientes, médicos, consultas y tratamientos",
      contact=openapi.Contact(email="soporte@saludvital.cl"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 1. Ruta al Panel de Administración de Django
    path('admin/', admin.site.urls),
    
    # 2. Ruta a los ENDPOINTS de la API (El requisito de "ruta hacia los ENDPOINT de la API")
    # Incluye el archivo api/urls.py que contiene todas las rutas del router
    path('api/', include('api.urls')),

    # 2.b. Rutas HTML para CRUD fuera del admin
    path('web/', include('api.web_urls')),
    
    # 3. Ruta al sistema "administrador" de DRF (El requisito de "ruta hacia el sistema administrador de DRF")
    # Esto es el login de la API navegable de Django REST Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # 4. Documentación de la API (Swagger y Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]