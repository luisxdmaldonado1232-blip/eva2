from rest_framework import serializers
from .models import (
    Especialidad,
    Medico,
    Paciente,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    Seguro, # NUEVO
    Horario, # NUEVO
    CitaMedica, # NUEVO
    HistorialClinico, # NUEVO
)

# ======================================================================
# 1. SERIALIZERS DE ENTIDADES BASE (Sin FKs)
# ======================================================================

class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Especialidad. """
    class Meta:
        model = Especialidad
        fields = '__all__' # Incluye 'id', 'nombre', 'descripcion'


class PacienteSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Paciente, incluyendo el campo CHOICES. """
    # Muestra el nombre legible del tipo de sangre en lugar del código (e.g., "A Positivo" en lugar de "A+")
    tipo_sangre_display = serializers.CharField(source='get_tipo_sangre_display', read_only=True)
    genero_display = serializers.CharField(source='get_genero_display', read_only=True) # NUEVO

    class Meta:
        model = Paciente
        # Se listan explícitamente los campos para un mejor control
        fields = [
            'id', 'rut', 'nombre', 'apellido', 'fecha_nacimiento', 
            'genero', 'genero_display', # NUEVO
            'tipo_sangre', 'tipo_sangre_display', 'correo', 'telefono', 
            'direccion', 'activo'
        ]

class MedicamentoSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Medicamento. """
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True) # NUEVO
    
    class Meta:
        model = Medicamento
        fields = ['id', 'nombre', 'laboratorio', 'categoria', 'categoria_display', 'stock', 'precio_unitario'] # ACTUALIZADO


# ======================================================================
# 2. SERIALIZERS DE ENTIDADES CON RELACIONES (Con FKs)
# ======================================================================

class MedicoSerializer(serializers.ModelSerializer):
    """ 
    Serializador para Medico. 
    Usa un campo de relación para mostrar el nombre de la Especialidad.
    """
    # SlugRelatedField muestra un campo específico del objeto relacionado (ej: el nombre)
    # En este caso, muestra el 'nombre' de la Especialidad en lugar de su 'id'
    especialidad_nombre = serializers.SlugRelatedField(
        source='especialidad',
        read_only=True,
        slug_field='nombre'
    )
    # También se incluye el ID de la FK para facilitar la escritura/actualización
    especialidad_id = serializers.PrimaryKeyRelatedField(
        source='especialidad',
        queryset=Especialidad.objects.all(),
        write_only=True # Solo se usa para POST/PUT, no se muestra en el GET principal
    )
    genero_display = serializers.CharField(source='get_genero_display', read_only=True) # NUEVO

    class Meta:
        model = Medico
        fields = [
            'id', 'nombre', 'apellido', 'rut', 'genero', 'genero_display', # ACTUALIZADO
            'correo', 'telefono', 'activo', 'especialidad_id', 'especialidad_nombre'
        ]
        
# ---

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    """ 
    Serializador para ConsultaMedica. 
    Usa campos anidados o de relación para Paciente y Medico.
    """
    # Campos de solo lectura para mostrar información del FK en lugar del ID
    paciente_nombre_completo = serializers.SerializerMethodField(read_only=True)
    medico_nombre_completo = serializers.SerializerMethodField(read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True) # Para el CHOICES
    prioridad_display = serializers.CharField(source='get_prioridad_display', read_only=True) # NUEVO

    class Meta:
        model = ConsultaMedica
        fields = [
            'id', 'paciente', 'paciente_nombre_completo', 'medico', 
            'medico_nombre_completo', 'fecha_consulta', 'motivo', 
            'diagnostico', 'estado', 'estado_display', 
            'prioridad', 'prioridad_display' # NUEVO
        ]
        # Campos 'paciente' y 'medico' serán IDs en la entrada (POST/PUT)
        extra_kwargs = {
            'paciente': {'write_only': True},
            'medico': {'write_only': True},
        }

    # Métodos para obtener los nombres completos del Paciente y el Médico
    def get_paciente_nombre_completo(self, obj):
        return f"{obj.paciente.nombre} {obj.paciente.apellido} ({obj.paciente.rut})"
    
    def get_medico_nombre_completo(self, obj):
        return f"Dr(a). {obj.medico.nombre} {obj.medico.apellido}"
    
# ---

class TratamientoSerializer(serializers.ModelSerializer):
    """ 
    Serializador para Tratamiento. 
    Muestra el ID de la consulta a la que está asociado.
    """
    consulta_id = serializers.PrimaryKeyRelatedField(
        source='consulta',
        queryset=ConsultaMedica.objects.all()
    )

    class Meta:
        model = Tratamiento
        fields = ['id', 'consulta_id', 'descripcion', 'duracion_dias', 'observaciones']

# ---

class RecetaMedicaSerializer(serializers.ModelSerializer):
    """ 
    Serializador para RecetaMedica (Tabla M:N). 
    Muestra el nombre del Medicamento asociado.
    """
    medicamento_nombre = serializers.SlugRelatedField(
        source='medicamento',
        read_only=True,
        slug_field='nombre'
    )
    via_administracion_display = serializers.CharField(source='get_via_administracion_display', read_only=True) # NUEVO

    class Meta:
        model = RecetaMedica
        fields = [
            'id', 'tratamiento', 'medicamento', 'medicamento_nombre', 
            'dosis', 'frecuencia', 'duracion', 
            'via_administracion', 'via_administracion_display' # NUEVO
        ]
        extra_kwargs = {
            # Los IDs de FK se usan para escribir, no para mostrar por defecto
            'tratamiento': {'write_only': True}, 
            'medicamento': {'write_only': True},
        }


# ======================================================================
# SERIALIZERS PARA NUEVAS TABLAS ADICIONALES
# ======================================================================

class SeguroSerializer(serializers.ModelSerializer):
    """
    Serializador para la nueva entidad Seguro.
    """
    paciente_nombre = serializers.SerializerMethodField(read_only=True)
    tipo_cobertura_display = serializers.CharField(source='get_tipo_cobertura_display', read_only=True)
    
    class Meta:
        model = Seguro
        fields = [
            'id', 'nombre_aseguradora', 'numero_poliza', 'tipo_cobertura', 
            'tipo_cobertura_display', 'fecha_inicio', 'fecha_vencimiento', 
            'porcentaje_cobertura', 'paciente', 'paciente_nombre', 'activo'
        ]
        extra_kwargs = {
            'paciente': {'write_only': True},
        }
    
    def get_paciente_nombre(self, obj):
        return f"{obj.paciente.nombre} {obj.paciente.apellido}"


class HorarioSerializer(serializers.ModelSerializer):
    """
    Serializador para la nueva entidad Horario.
    """
    medico_nombre = serializers.SerializerMethodField(read_only=True)
    dia_semana_display = serializers.CharField(source='get_dia_semana_display', read_only=True)
    
    class Meta:
        model = Horario
        fields = [
            'id', 'medico', 'medico_nombre', 'dia_semana', 'dia_semana_display',
            'hora_inicio', 'hora_fin', 'duracion_consulta_minutos', 'activo'
        ]
        extra_kwargs = {
            'medico': {'write_only': True},
        }
    
    def get_medico_nombre(self, obj):
        return f"Dr(a). {obj.medico.nombre} {obj.medico.apellido}"


class CitaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para la nueva entidad CitaMedica.
    """
    paciente_nombre_completo = serializers.SerializerMethodField(read_only=True)
    medico_nombre_completo = serializers.SerializerMethodField(read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)
    
    class Meta:
        model = CitaMedica
        fields = [
            'id', 'paciente', 'paciente_nombre_completo', 'medico', 
            'medico_nombre_completo', 'fecha_hora_cita', 'motivo', 
            'estado', 'estado_display', 'observaciones', 'fecha_creacion',
            'consulta_realizada'
        ]
        extra_kwargs = {
            'paciente': {'write_only': True},
            'medico': {'write_only': True},
        }
    
    def get_paciente_nombre_completo(self, obj):
        return f"{obj.paciente.nombre} {obj.paciente.apellido}"
    
    def get_medico_nombre_completo(self, obj):
        return f"Dr(a). {obj.medico.nombre} {obj.medico.apellido}"


class HistorialClinicoSerializer(serializers.ModelSerializer):
    """
    Serializador para la nueva entidad HistorialClinico.
    """
    paciente_nombre = serializers.SerializerMethodField(read_only=True)
    registrado_por_nombre = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = HistorialClinico
        fields = [
            'id', 'paciente', 'paciente_nombre', 'fecha_registro', 
            'tipo_registro', 'descripcion', 'medicamentos_asociados',
            'registrado_por', 'registrado_por_nombre'
        ]
        extra_kwargs = {
            'paciente': {'write_only': True},
            'registrado_por': {'write_only': True},
        }
    
    def get_paciente_nombre(self, obj):
        return f"{obj.paciente.nombre} {obj.paciente.apellido}"
    
    def get_registrado_por_nombre(self, obj):
        if obj.registrado_por:
            return f"Dr(a). {obj.registrado_por.nombre} {obj.registrado_por.apellido}"
        return "No especificado"
