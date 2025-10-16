from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewSet,
    PacienteViewSet,
    MedicoViewSet,
    ConsultaMedicaViewSet,
    TratamientoViewSet,
    MedicamentoViewSet,
    RecetaMedicaViewSet,
    SeguroViewSet, # NUEVO
    HorarioViewSet, # NUEVO
    CitaMedicaViewSet, # NUEVO
    HistorialClinicoViewSet, # NUEVO
)

# Creamos una instancia del DefaultRouter
# Este objeto se encarga de registrar los ViewSets y generar las URLs de lista y detalle
router = DefaultRouter()

# 1. Registro de ViewSets: 
# El primer argumento es el prefijo de la URL (endpoint) y el segundo es la clase ViewSet
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'consultas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'recetas', RecetaMedicaViewSet)

# Registro de las NUEVAS entidades adicionales
router.register(r'seguros', SeguroViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'citas', CitaMedicaViewSet)
router.register(r'historiales', HistorialClinicoViewSet)

# La lista de patrones de URL
urlpatterns = [
    # Esta línea incluye todas las rutas generadas automáticamente por el Router
    # Ejemplos de rutas generadas:
    # - /especialidades/ (GET, POST)
    # - /especialidades/{pk}/ (GET, PUT, PATCH, DELETE)
    path('', include(router.urls)),
]