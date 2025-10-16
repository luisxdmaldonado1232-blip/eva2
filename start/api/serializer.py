from rest_framework import serializers
from .models import (
    Especialidad,
    Medico,
    Paciente,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    Ubicacion # Modelo adicional
)

# ======================================================================
# 1. SERIALIZERS DE ENTIDADES BASE (Sin FKs)
# ======================================================================

class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Especialidad. """
    class Meta:
        model = Especialidad
        fields = '__all__' # Incluye 'id', 'nombre', 'descripcion'

class UbicacionSerializer(serializers.ModelSerializer):
    """ Serializador para la nueva entidad Ubicacion. """
    class Meta:
        model = Ubicacion
        fields = '__all__' # Incluye 'id', 'nombre_ubicacion', 'direccion_completa'

class PacienteSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Paciente, incluyendo el campo CHOICES. """
    # Muestra el nombre legible del tipo de sangre en lugar del código (e.g., "A Positivo" en lugar de "A+")
    tipo_sangre_display = serializers.CharField(source='get_tipo_sangre_display', read_only=True)

    class Meta:
        model = Paciente
        # Se listan explícitamente los campos para un mejor control
        fields = [
            'id', 'rut', 'nombre', 'apellido', 'fecha_nacimiento', 
            'tipo_sangre', 'tipo_sangre_display', 'correo', 'telefono', 
            'direccion', 'activo'
        ]

class MedicamentoSerializer(serializers.ModelSerializer):
    """ Serializador para la entidad Medicamento. """
    class Meta:
        model = Medicamento
        fields = '__all__' # Incluye 'id', 'nombre', 'laboratorio', 'stock', 'precio_unitario'


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

    class Meta:
        model = Medico
        fields = [
            'id', 'nombre', 'apellido', 'rut', 'correo', 'telefono', 
            'activo', 'especialidad_id', 'especialidad_nombre'
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

    class Meta:
        model = ConsultaMedica
        fields = [
            'id', 'paciente', 'paciente_nombre_completo', 'medico', 
            'medico_nombre_completo', 'fecha_consulta', 'motivo', 
            'diagnostico', 'estado', 'estado_display'
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

    class Meta:
        model = RecetaMedica
        fields = [
            'id', 'tratamiento', 'medicamento', 'medicamento_nombre', 
            'dosis', 'frecuencia', 'duracion'
        ]
        extra_kwargs = {
            # Los IDs de FK se usan para escribir, no para mostrar por defecto
            'tratamiento': {'write_only': True}, 
            'medicamento': {'write_only': True},
        }