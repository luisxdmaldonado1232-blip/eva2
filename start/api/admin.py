from django.contrib import admin
from .models import (
    Especialidad,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    Seguro,
    Horario,
    CitaMedica,
    HistorialClinico,
)

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'genero', 'especialidad', 'telefono', 'activo')
    list_display_links = ('rut', 'nombre', 'apellido')
    search_fields = ('rut', 'nombre', 'apellido', 'correo')
    list_filter = ('especialidad', 'genero', 'activo')
    ordering = ('apellido',)

class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'fecha_consulta', 'estado', 'prioridad')
    search_fields = ('paciente__rut', 'medico__rut', 'motivo')
    list_filter = ('estado', 'prioridad', 'fecha_consulta')
    date_hierarchy = 'fecha_consulta'

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'genero', 'tipo_sangre', 'telefono', 'activo')
    list_display_links = ('rut', 'nombre', 'apellido')
    search_fields = ('rut', 'nombre', 'apellido', 'correo')
    list_filter = ('genero', 'tipo_sangre', 'activo')
    ordering = ('apellido',)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'categoria', 'stock', 'precio_unitario')
    list_display_links = ('nombre',)
    search_fields = ('nombre', 'laboratorio')
    list_filter = ('categoria', 'laboratorio')
    ordering = ('nombre',)

class SeguroAdmin(admin.ModelAdmin):
    list_display = ('numero_poliza', 'paciente', 'nombre_aseguradora', 'tipo_cobertura', 'porcentaje_cobertura', 'fecha_vencimiento', 'activo')
    list_display_links = ('numero_poliza',)
    search_fields = ('numero_poliza', 'nombre_aseguradora', 'paciente__rut', 'paciente__nombre')
    list_filter = ('tipo_cobertura', 'activo', 'nombre_aseguradora')
    date_hierarchy = 'fecha_vencimiento'
    ordering = ('-fecha_vencimiento',)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('medico', 'dia_semana', 'hora_inicio', 'hora_fin', 'duracion_consulta_minutos', 'activo')
    list_filter = ('dia_semana', 'activo', 'medico__especialidad')
    search_fields = ('medico__nombre', 'medico__apellido', 'medico__rut')
    ordering = ('medico', 'dia_semana', 'hora_inicio')

class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'fecha_hora_cita', 'estado', 'consulta_realizada')
    list_display_links = ('id',)
    search_fields = ('paciente__rut', 'paciente__nombre', 'medico__rut', 'medico__apellido', 'motivo')
    list_filter = ('estado', 'fecha_hora_cita', 'medico__especialidad')
    date_hierarchy = 'fecha_hora_cita'
    ordering = ('-fecha_hora_cita',)

class HistorialClinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'tipo_registro', 'fecha_registro', 'registrado_por')
    list_display_links = ('id', 'tipo_registro')
    search_fields = ('paciente__rut', 'paciente__nombre', 'tipo_registro', 'descripcion')
    list_filter = ('tipo_registro', 'fecha_registro', 'registrado_por')
    date_hierarchy = 'fecha_registro'
    ordering = ('-fecha_registro',)

admin.site.register(Medico, MedicoAdmin)
admin.site.register(ConsultaMedica, ConsultaMedicaAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Seguro, SeguroAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(CitaMedica, CitaMedicaAdmin)
admin.site.register(HistorialClinico, HistorialClinicoAdmin)
admin.site.register(Especialidad)
admin.site.register(Tratamiento)
admin.site.register(RecetaMedica)
