from rest_framework import viewsets
from .models import (
    Especialidad,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
    Seguro, # NUEVO
    Horario, # NUEVO
    CitaMedica, # NUEVO
    HistorialClinico, # NUEVO
)
from .serializer import (
    EspecialidadSerializer,
    PacienteSerializer,
    MedicoSerializer,
    ConsultaMedicaSerializer,
    TratamientoSerializer,
    MedicamentoSerializer,
    RecetaMedicaSerializer,
    SeguroSerializer, # NUEVO
    HorarioSerializer, # NUEVO
    CitaMedicaSerializer, # NUEVO
    HistorialClinicoSerializer, # NUEVO
)

# ======================================================================
# VIEWSETS PARA CADA ENTIDAD
# Cada ViewSet hereda de ModelViewSet para proporcionar las operaciones
# CRUD (Create, Retrieve, Update, Destroy, List) automáticamente.
# ======================================================================

class EspecialidadViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad Especialidad. """
    # Queryset: Define el conjunto de objetos que el ViewSet puede manejar
    queryset = Especialidad.objects.all()
    # Serializer: Define cómo se serializan los datos
    serializer_class = EspecialidadSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad Paciente. """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    # Mejora: permite buscar por RUT, nombre o apellido (Requisito: Filtros y búsquedas)
    search_fields = ['rut', 'nombre', 'apellido']

class MedicoViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad Medico. """
    # Usamos select_related para optimizar la consulta (cargar la Especialidad en una sola consulta)
    queryset = Medico.objects.select_related('especialidad').all()
    serializer_class = MedicoSerializer
    
    # Mejora: permite buscar por RUT, nombre o apellido y filtrar por especialidad (Requisito: Filtros y búsquedas)
    search_fields = ['rut', 'nombre', 'apellido', 'especialidad__nombre']
    filterset_fields = ['especialidad', 'activo'] # Filtra por ID de especialidad o por estado activo

class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad ConsultaMedica. """
    # Optimización: Carga Paciente y Medico en una sola consulta
    queryset = ConsultaMedica.objects.select_related('paciente', 'medico').all()
    serializer_class = ConsultaMedicaSerializer
    
    # Mejora: permite filtrar por médico, paciente o estado (Requisito: Filtros y búsquedas)
    filterset_fields = ['medico', 'paciente', 'estado']


class TratamientoViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad Tratamiento. """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer


class MedicamentoViewSet(viewsets.ModelViewSet):
    """ ViewSet para la entidad Medicamento. """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    
    # Mejora: permite buscar por nombre o laboratorio
    search_fields = ['nombre', 'laboratorio']


class RecetaMedicaViewSet(viewsets.ModelViewSet):
    """ 
    ViewSet para la entidad RecetaMedica. 
    Representa el detalle de la relación entre Tratamiento y Medicamento.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer


# ======================================================================
# VIEWSETS PARA NUEVAS TABLAS ADICIONALES
# ======================================================================

class SeguroViewSet(viewsets.ModelViewSet):
    """ ViewSet para la nueva entidad Seguro. """
    queryset = Seguro.objects.select_related('paciente').all()
    serializer_class = SeguroSerializer
    
    # Permite filtrar por paciente y buscar por aseguradora
    filterset_fields = ['paciente', 'activo', 'tipo_cobertura']
    search_fields = ['nombre_aseguradora', 'numero_poliza']


class HorarioViewSet(viewsets.ModelViewSet):
    """ ViewSet para la nueva entidad Horario. """
    queryset = Horario.objects.select_related('medico').all()
    serializer_class = HorarioSerializer
    
    # Permite filtrar por médico y día de la semana
    filterset_fields = ['medico', 'dia_semana', 'activo']


class CitaMedicaViewSet(viewsets.ModelViewSet):
    """ ViewSet para la nueva entidad CitaMedica. """
    queryset = CitaMedica.objects.select_related('paciente', 'medico', 'consulta_realizada').all()
    serializer_class = CitaMedicaSerializer
    
    # Permite filtrar por médico, paciente y estado
    filterset_fields = ['medico', 'paciente', 'estado']
    search_fields = ['paciente__rut', 'paciente__nombre', 'medico__rut']


class HistorialClinicoViewSet(viewsets.ModelViewSet):
    """ ViewSet para la nueva entidad HistorialClinico. """
    queryset = HistorialClinico.objects.select_related('paciente', 'registrado_por').all()
    serializer_class = HistorialClinicoSerializer
    
    # Permite filtrar por paciente y buscar por tipo de registro
    filterset_fields = ['paciente', 'registrado_por', 'tipo_registro']
    search_fields = ['tipo_registro', 'descripcion']
