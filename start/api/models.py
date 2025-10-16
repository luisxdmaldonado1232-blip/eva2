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

# CHOICES para el campo 'genero' en Paciente y Medico - NUEVA MEJORA
GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
    ('NE', 'Prefiero no especificar'),
]

# CHOICES para el campo 'estado' en el modelo ConsultaMedica
ESTADO_CONSULTA_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
]

# CHOICES para el campo 'prioridad' en ConsultaMedica - NUEVA MEJORA
PRIORIDAD_CHOICES = [
    ('BAJA', 'Baja'),
    ('NORMAL', 'Normal'),
    ('ALTA', 'Alta'),
    ('URGENTE', 'Urgente'),
]

# CHOICES para el campo 'categoria' en Medicamento - NUEVA MEJORA
CATEGORIA_MEDICAMENTO_CHOICES = [
    ('ANALGESICO', 'Analgésico'),
    ('ANTIBIOTICO', 'Antibiótico'),
    ('ANTIINFLAMATORIO', 'Antiinflamatorio'),
    ('ANTIHIPERTENSIVO', 'Antihipertensivo'),
    ('VITAMINA', 'Vitamina/Suplemento'),
    ('ANTIHISTAMINICO', 'Antihistamínico'),
    ('OTRO', 'Otro'),
]

# CHOICES para el campo 'via_administracion' en RecetaMedica - NUEVA MEJORA
VIA_ADMINISTRACION_CHOICES = [
    ('ORAL', 'Vía Oral'),
    ('TOPICA', 'Vía Tópica'),
    ('INTRAVENOSA', 'Vía Intravenosa'),
    ('INTRAMUSCULAR', 'Vía Intramuscular'),
    ('SUBCUTANEA', 'Vía Subcutánea'),
    ('SUBLINGUAL', 'Vía Sublingual'),
    ('INHALATORIA', 'Vía Inhalatoria'),
]

# CHOICES para el campo 'dia_semana' en Horario - NUEVA TABLA
DIA_SEMANA_CHOICES = [
    (1, 'Lunes'),
    (2, 'Martes'),
    (3, 'Miércoles'),
    (4, 'Jueves'),
    (5, 'Viernes'),
    (6, 'Sábado'),
    (7, 'Domingo'),
]

# CHOICES para el campo 'estado' en CitaMedica - NUEVA TABLA
ESTADO_CITA_CHOICES = [
    ('AGENDADA', 'Agendada'),
    ('CONFIRMADA', 'Confirmada'),
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
    ('NO_ASISTIO', 'No Asistió'),
]

# CHOICES para el campo 'tipo_cobertura' en Seguro - NUEVA TABLA
TIPO_COBERTURA_CHOICES = [
    ('BASICA', 'Cobertura Básica'),
    ('INTERMEDIA', 'Cobertura Intermedia'),
    ('COMPLETA', 'Cobertura Completa'),
    ('PREMIUM', 'Cobertura Premium'),
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

class Laboratorio(models.Model):
    """
    Modelo para registrar la información de los laboratorios clínicos.
    """
    # id (int, PK) se crea automáticamente por Django
    nombre = models.CharField(max_length=100, unique=True) # string, nombre
    direccion = models.CharField(max_length=255, blank=True, null=True) # string, direccion
    telefono = models.CharField(max_length=15, blank=True, null=True) # string, telefono
    correo = models.EmailField(max_length=100, unique=True, blank=True, null=True) # string, correo
    

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    """
    Modelo para registrar la información personal y de contacto de un paciente.
    Incluye un CHOICES para el tipo de sangre y género.
    """
    # id (int, PK) se crea automáticamente por Django
    rut = models.CharField(max_length=12, unique=True) # string, rut
    nombre = models.CharField(max_length=100) # string, nombre
    apellido = models.CharField(max_length=100) # string, apellido
    fecha_nacimiento = models.DateField() # date, fecha_nacimiento
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES, default='NE') # string, genero (NUEVO)
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
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES, default='NE') # string, genero (NUEVO)
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
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='NORMAL') # string, prioridad (NUEVO)

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
    categoria = models.CharField(max_length=20, choices=CATEGORIA_MEDICAMENTO_CHOICES, default='OTRO') # string, categoria (NUEVO)
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
    via_administracion = models.CharField(max_length=15, choices=VIA_ADMINISTRACION_CHOICES, default='ORAL') # string, via_administracion (NUEVO)

    def __str__(self):
        return f"Receta para {self.medicamento.nombre} - Trat. {self.tratamiento.id}"


# ======================================================================
# NUEVAS TABLAS ADICIONALES (Requisito: Nuevas tablas adicionales)
# ======================================================================

class Seguro(models.Model):
    """
    NUEVA TABLA: Modelo para registrar los seguros médicos de los pacientes.
    Permite gestionar coberturas y planes de salud.
    """
    # id (int, PK) se crea automáticamente por Django
    nombre_aseguradora = models.CharField(max_length=100) # string, nombre_aseguradora
    numero_poliza = models.CharField(max_length=50, unique=True) # string, numero_poliza
    tipo_cobertura = models.CharField(max_length=15, choices=TIPO_COBERTURA_CHOICES, default='BASICA') # string, tipo_cobertura
    fecha_inicio = models.DateField() # date, fecha_inicio
    fecha_vencimiento = models.DateField() # date, fecha_vencimiento
    porcentaje_cobertura = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # decimal, porcentaje_cobertura (0-100)
    
    # FK (int, paciente_id): Relación con Paciente - Un paciente puede tener un seguro
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='seguros')
    
    activo = models.BooleanField(default=True) # boolean, activo

    def __str__(self):
        return f"{self.nombre_aseguradora} - Póliza {self.numero_poliza} ({self.paciente.apellido})"
    
    class Meta:
        verbose_name_plural = "Seguros"


class Horario(models.Model):
    """
    NUEVA TABLA: Modelo para registrar los horarios de atención de los médicos.
    Permite gestionar la disponibilidad del personal médico.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, medico_id): Relación con Medico
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='horarios')
    
    dia_semana = models.IntegerField(choices=DIA_SEMANA_CHOICES) # int, dia_semana (1=Lunes, 7=Domingo)
    hora_inicio = models.TimeField() # time, hora_inicio
    hora_fin = models.TimeField() # time, hora_fin
    duracion_consulta_minutos = models.IntegerField(default=30) # int, duracion_consulta_minutos (duración de cada consulta)
    
    activo = models.BooleanField(default=True) # boolean, activo

    def __str__(self):
        return f"Dr(a). {self.medico.apellido} - {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"
    
    class Meta:
        verbose_name_plural = "Horarios"
        ordering = ['dia_semana', 'hora_inicio']


class CitaMedica(models.Model):
    """
    NUEVA TABLA: Modelo para gestionar las citas médicas (agendamiento previo).
    Se diferencia de ConsultaMedica en que esta es la reserva previa, 
    mientras que ConsultaMedica es el registro de la atención realizada.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, paciente_id): Relación con Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='citas')
    
    # FK (int, medico_id): Relación con Medico
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='citas')
    
    fecha_hora_cita = models.DateTimeField() # datetime, fecha_hora_cita
    motivo = models.CharField(max_length=255) # string, motivo
    estado = models.CharField(max_length=15, choices=ESTADO_CITA_CHOICES, default='AGENDADA') # string, estado
    observaciones = models.TextField(blank=True, null=True) # text, observaciones
    fecha_creacion = models.DateTimeField(auto_now_add=True) # datetime, fecha_creacion (timestamp automático)
    
    # FK opcional: Si la cita se realizó, puede vincularse a la ConsultaMedica resultante
    consulta_realizada = models.OneToOneField(
        ConsultaMedica, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='cita_origen'
    )

    def __str__(self):
        return f"Cita N°{self.id} - {self.paciente.apellido} con Dr(a). {self.medico.apellido} ({self.fecha_hora_cita.strftime('%d/%m/%Y %H:%M')})"
    
    class Meta:
        verbose_name_plural = "Citas Médicas"
        ordering = ['-fecha_hora_cita']


class HistorialClinico(models.Model):
    """
    NUEVA TABLA: Modelo para registrar eventos importantes en el historial clínico del paciente.
    Incluye alergias, enfermedades crónicas, cirugías previas, etc.
    """
    # id (int, PK) se crea automáticamente por Django
    
    # FK (int, paciente_id): Relación con Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historial_clinico')
    
    fecha_registro = models.DateField(default=timezone.now) # date, fecha_registro
    tipo_registro = models.CharField(max_length=100) # string, tipo_registro (ej: 'Alergia', 'Cirugía', 'Enfermedad Crónica')
    descripcion = models.TextField() # text, descripcion
    medicamentos_asociados = models.CharField(max_length=255, blank=True, null=True) # string, medicamentos_asociados
    
    # FK opcional: Médico que registró el evento
    registrado_por = models.ForeignKey(
        Medico, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='registros_clinicos'
    )

    def __str__(self):
        return f"Historial de {self.paciente.apellido} - {self.tipo_registro} ({self.fecha_registro})"
    
    class Meta:
        verbose_name_plural = "Historiales Clínicos"
        ordering = ['-fecha_registro']
