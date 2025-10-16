from django.db import models
from django.utils import timezone

# ======================================================================
# BLOQUE DE CONSTANTES DE CHOICES
# Se definen las opciones para campos que deben tener un conjunto fijo de valores.
# ======================================================================

# CHOICES para el campo 'tipo_sangre' en el modelo Paciente (Requisito: Inclusión de CHOICES)
TIPO_SANGRE_CHOICES = [
    ('A+', 'A Positivo'),
    ('A-', 'A Negativo'),
    ('B+', 'B Positivo'),
    ('B-', 'B Negativo'),
    ('AB+', 'AB Positivo'),
    ('AB-', 'AB Negativo'),
    ('O+', 'O Positivo'),
    ('O-', 'O Negativo'),
]

# CHOICES para el campo 'estado' en el modelo ConsultaMedica
ESTADO_CONSULTA_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
]

# ======================================================================
# MODELOS BASE DEL DIAGRAMA
# Se definen los modelos principales de la clínica Salud Vital Ltda.
# Cada modelo representa una tabla en la base de datos.
# ======================================================================

class Especialidad(models.Model):
    """
    Modelo para registrar las diferentes especialidades médicas disponibles.
    Contiene un nombre único y una descripción de la especialidad.
    """
    # id (int, PK) se crea automáticamente por Django
    nombre = models.CharField(max_length=100, unique=True) # string, nombre
    descripcion = models.CharField(max_length=255, blank=True, null=True) # string, descripcion

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    """
    NUEVA TABLA/ENTIDAD: Modelo adicional para almacenar las ubicaciones de los médicos
    (ej: sede, piso, box) o la dirección detallada de los pacientes,
    mejorando el diseño modular. (Requisito: Nuevas tablas adicionales)
    """
    nombre_ubicacion = models.CharField(max_length=100)
    direccion_completa = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nombre_ubicacion

class Paciente(models.Model):
    """
    Modelo para registrar la información personal y de contacto de un paciente.
    Incluye un CHOICES para el tipo de sangre.
    """
    # id (int, PK) se crea automáticamente por Django
    rut = models.CharField(max_length=12, unique=True) # string, rut
    nombre = models.CharField(max_length=100) # string, nombre
    apellido = models.CharField(max_length=100) # string, apellido
    fecha_nacimiento = models.DateField() # date, fecha_nacimiento
    tipo_sangre = models.CharField(max_length=3, choices=TIPO_SANGRE_CHOICES) # string, tipo_sangre (con CHOICES)
    correo = models.EmailField(max_length=100, unique=True) # string, correo
    telefono = models.CharField(max_length=15) # string, telefono
    direccion = models.CharField(max_length=255) # string, direccion
    activo = models.BooleanField(default=True) # boolean, activo

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

class Medico(models.Model):
    """
    Modelo para registrar la información de un médico.
    Tiene una relación de uno a muchos con Especialidad (un médico tiene una especialidad).
    """
    # id (int, PK) se crea automáticamente por Django
    nombre = models.CharField(max_length=100) # string, nombre
    apellido = models.CharField(max_length=100) # string, apellido
    rut = models.CharField(max_length=12, unique=True) # string, rut
    correo = models.EmailField(max_length=100, unique=True) # string, correo
    telefono = models.CharField(max_length=15) # string, telefono
    activo = models.BooleanField(default=True) # boolean, activo
    
    # FK (int, especialidad_id): Relación con Especialidad
    # on_delete=models.PROTECT evita borrar una especialidad si hay médicos asociados.
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT) 

    def __str__(self):
        return f"Dr(a). {self.nombre} {self.apellido} - {self.especialidad.nombre}"

class ConsultaMedica(models.Model):
    """
    Modelo para registrar una atención médica específica.
    Tiene relaciones de muchos a uno con Paciente y Medico.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, paciente_id): Relación con Paciente
    # on_delete=models.PROTECT para no borrar consultas al eliminar un paciente (por historial).
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT) 
    
    # FK (int, medico_id): Relación con Medico
    # on_delete=models.PROTECT para no borrar consultas al eliminar un médico (por historial).
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT) 
    
    fecha_consulta = models.DateTimeField(default=timezone.now) # datetime, fecha_consulta
    motivo = models.CharField(max_length=255) # string, motivo
    diagnostico = models.CharField(max_length=500, blank=True, null=True) # string, diagnostico
    estado = models.CharField(max_length=10, choices=ESTADO_CONSULTA_CHOICES, default='PENDIENTE') # string, estado

    def __str__(self):
        return f"Consulta N°{self.id} - {self.paciente.apellido} con Dr(a). {self.medico.apellido}"

class Tratamiento(models.Model):
    """
    Modelo para registrar un tratamiento derivado de una consulta médica.
    Relación de uno a muchos con ConsultaMedica.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, consulta_id): Relación con ConsultaMedica
    # on_delete=models.CASCADE para que si se elimina la consulta, se elimine su tratamiento.
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE) 
    
    descripcion = models.CharField(max_length=500) # string, descripcion
    duracion_dias = models.IntegerField() # int, duracion_dias
    observaciones = models.TextField(blank=True, null=True) # string, observaciones

    def __str__(self):
        return f"Tratamiento de Consulta N°{self.consulta.id} - {self.descripcion[:30]}..."

class Medicamento(models.Model):
    """
    Modelo para registrar la información de un medicamento.
    """
    # id (int, PK) se crea automáticamente por Django
    nombre = models.CharField(max_length=100) # string, nombre
    laboratorio = models.CharField(max_length=100) # string, laboratorio
    stock = models.IntegerField(default=0) # int, stock
    # decimal, precio_unitario - Uso de DecimalField para mayor precisión monetaria.
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio})"

class RecetaMedica(models.Model):
    """
    Modelo que representa la relación (tabla intermedia) entre un Tratamiento y los Medicamentos.
    Es una tabla de detalle para la relación muchos a muchos implícita.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, tratamiento_id): Relación con Tratamiento
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE) 
    
    # FK (int, medicamento_id): Relación con Medicamento
    # on_delete=models.PROTECT para no eliminar medicamentos al anular una receta.
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT) 
    
    dosis = models.CharField(max_length=100) # string, dosis
    frecuencia = models.CharField(max_length=100) # string, frecuencia
    duracion = models.CharField(max_length=100) # string, duracion (ej: '7 días', '1 mes')

    def __str__(self):
        return f"Receta para {self.medicamento.nombre} - Trat. {self.tratamiento.id}"