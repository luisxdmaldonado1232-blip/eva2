from rest_framework import viewsets
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
from .serializer import (
    EspecialidadSerializer,
    UbicacionSerializer,
    PacienteSerializer,
    MedicoSerializer,
    ConsultaMedicaSerializer,
    TratamientoSerializer,
    MedicamentoSerializer,
    RecetaMedicaSerializer,
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

class UbicacionViewSet(viewsets.ModelViewSet):
    """ ViewSet para la nueva entidad Ubicacion. """
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

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