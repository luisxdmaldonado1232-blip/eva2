from django.contrib import admin
from django.urls import path, include

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]