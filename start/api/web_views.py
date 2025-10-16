from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .models import (
    Especialidad,
    Paciente,
    Medico,
    ConsultaMedica,
    Tratamiento,
    Medicamento,
    RecetaMedica,
)


class HomeView(TemplateView):
    template_name = "index.html"


# ==========================
# Especialidad CRUD
# ==========================
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = "especialidad_list.html"
    context_object_name = "items"


class EspecialidadCreateView(CreateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "especialidad_form.html"
    success_url = reverse_lazy("especialidad_list")


class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    fields = ["nombre", "descripcion"]
    template_name = "especialidad_form.html"
    success_url = reverse_lazy("especialidad_list")


class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = "especialidad_confirm_delete.html"
    success_url = reverse_lazy("especialidad_list")


# ==========================
# Paciente CRUD
# ==========================
class PacienteListView(ListView):
    model = Paciente
    template_name = "paciente_list.html"
    context_object_name = "items"


class PacienteCreateView(CreateView):
    model = Paciente
    fields = [
        "rut",
        "nombre",
        "apellido",
        "fecha_nacimiento",
        "genero",
        "tipo_sangre",
        "correo",
        "telefono",
        "direccion",
        "activo",
    ]
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente_list")


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = [
        "rut",
        "nombre",
        "apellido",
        "fecha_nacimiento",
        "genero",
        "tipo_sangre",
        "correo",
        "telefono",
        "direccion",
        "activo",
    ]
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente_list")


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = "paciente_confirm_delete.html"
    success_url = reverse_lazy("paciente_list")


# ==========================
# Medico CRUD
# ==========================
class MedicoListView(ListView):
    model = Medico
    template_name = "medico_list.html"
    context_object_name = "items"


class MedicoCreateView(CreateView):
    model = Medico
    fields = [
        "nombre",
        "apellido",
        "rut",
        "genero",
        "correo",
        "telefono",
        "activo",
        "especialidad",
    ]
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico_list")


class MedicoUpdateView(UpdateView):
    model = Medico
    fields = [
        "nombre",
        "apellido",
        "rut",
        "genero",
        "correo",
        "telefono",
        "activo",
        "especialidad",
    ]
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico_list")


class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "medico_confirm_delete.html"
    success_url = reverse_lazy("medico_list")


# ==========================
# ConsultaMedica CRUD
# ==========================
class ConsultaListView(ListView):
    model = ConsultaMedica
    template_name = "consulta_list.html"
    context_object_name = "items"


class ConsultaCreateView(CreateView):
    model = ConsultaMedica
    fields = [
        "paciente",
        "medico",
        "fecha_consulta",
        "motivo",
        "diagnostico",
        "estado",
        "prioridad",
    ]
    template_name = "consulta_form.html"
    success_url = reverse_lazy("consulta_list")


class ConsultaUpdateView(UpdateView):
    model = ConsultaMedica
    fields = [
        "paciente",
        "medico",
        "fecha_consulta",
        "motivo",
        "diagnostico",
        "estado",
        "prioridad",
    ]
    template_name = "consulta_form.html"
    success_url = reverse_lazy("consulta_list")


class ConsultaDeleteView(DeleteView):
    model = ConsultaMedica
    template_name = "consulta_confirm_delete.html"
    success_url = reverse_lazy("consulta_list")


# ==========================
# Tratamiento CRUD
# ==========================
class TratamientoListView(ListView):
    model = Tratamiento
    template_name = "tratamiento_list.html"
    context_object_name = "items"


class TratamientoCreateView(CreateView):
    model = Tratamiento
    fields = ["consulta", "descripcion", "duracion_dias", "observaciones"]
    template_name = "tratamiento_form.html"
    success_url = reverse_lazy("tratamiento_list")


class TratamientoUpdateView(UpdateView):
    model = Tratamiento
    fields = ["consulta", "descripcion", "duracion_dias", "observaciones"]
    template_name = "tratamiento_form.html"
    success_url = reverse_lazy("tratamiento_list")


class TratamientoDeleteView(DeleteView):
    model = Tratamiento
    template_name = "tratamiento_confirm_delete.html"
    success_url = reverse_lazy("tratamiento_list")


# ==========================
# Medicamento CRUD
# ==========================
class MedicamentoListView(ListView):
    model = Medicamento
    template_name = "medicamento_list.html"
    context_object_name = "items"


class MedicamentoCreateView(CreateView):
    model = Medicamento
    fields = ["nombre", "laboratorio", "categoria", "stock", "precio_unitario"]
    template_name = "medicamento_form.html"
    success_url = reverse_lazy("medicamento_list")


class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    fields = ["nombre", "laboratorio", "categoria", "stock", "precio_unitario"]
    template_name = "medicamento_form.html"
    success_url = reverse_lazy("medicamento_list")


class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = "medicamento_confirm_delete.html"
    success_url = reverse_lazy("medicamento_list")


# ==========================
# RecetaMedica CRUD
# ==========================
class RecetaListView(ListView):
    model = RecetaMedica
    template_name = "receta_list.html"
    context_object_name = "items"


class RecetaCreateView(CreateView):
    model = RecetaMedica
    fields = [
        "tratamiento",
        "medicamento",
        "dosis",
        "frecuencia",
        "duracion",
        "via_administracion",
    ]
    template_name = "receta_form.html"
    success_url = reverse_lazy("receta_list")


class RecetaUpdateView(UpdateView):
    model = RecetaMedica
    fields = [
        "tratamiento",
        "medicamento",
        "dosis",
        "frecuencia",
        "duracion",
        "via_administracion",
    ]
    template_name = "receta_form.html"
    success_url = reverse_lazy("receta_list")


class RecetaDeleteView(DeleteView):
    model = RecetaMedica
    template_name = "receta_confirm_delete.html"
    success_url = reverse_lazy("receta_list")
