from django.contrib import admin
from .models import (
    Especialidad,
    Ubicacion,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
)

# ======================================================================
# 1. CLASES ADMIN (Modelos con personalización)
# ======================================================================

class MedicoAdmin(admin.ModelAdmin):
    """
    Configuración avanzada para la administración del modelo Medico.
    Permite buscar por RUT y filtrar por Especialidad y estado 'activo'.
    """
    # Muestra los campos en formato de columna
    list_display = (
        'rut', 
        'nombre', 
        'apellido', 
        'especialidad', 
        'telefono', 
        'activo'
    )
    
    # Permite hacer clic en el nombre para editar
    list_display_links = ('rut', 'nombre', 'apellido')
    
    # Añade una caja de búsqueda
    search_fields = ('rut', 'nombre', 'apellido', 'correo')
    
    # Añade filtros laterales
    list_filter = ('especialidad', 'activo')
    
    # Orden predeterminado (por apellido ascendente)
    ordering = ('apellido',)
    
# ---

class ConsultaMedicaAdmin(admin.ModelAdmin):
    """
    Configuración para facilitar la búsqueda de consultas.
    """
    list_display = (
        'id', 
        'paciente', 
        'medico', 
        'fecha_consulta', 
        'estado'
    )
    search_fields = ('paciente__rut', 'medico__rut', 'motivo')
    list_filter = ('estado', 'fecha_consulta')
    date_hierarchy = 'fecha_consulta' # Permite navegar por fechas

# ======================================================================
# 2. REGISTRO DE MODELOS
# ======================================================================

# Registrar Medico con su configuración personalizada
admin.site.register(Medico, MedicoAdmin)
admin.site.register(ConsultaMedica, ConsultaMedicaAdmin)

# Registrar otros modelos sin configuración personalizada (registro simple)
admin.site.register(Especialidad)
admin.site.register(Ubicacion)
admin.site.register(Paciente)
admin.site.register(Tratamiento)
admin.site.register(Medicamento)
admin.site.register(RecetaMedica)