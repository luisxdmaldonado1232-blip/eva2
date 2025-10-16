from django.urls import path

from .web_views import (
    HomeView,
    # Especialidad
    EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView,
    # Paciente
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    # Medico
    MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView,
    # Consulta
    ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView,
    # Tratamiento
    TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView,
    # Medicamento
    MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView,
    # Receta
    RecetaListView, RecetaCreateView, RecetaUpdateView, RecetaDeleteView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Especialidad
    path('especialidades/', EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidades/nuevo/', EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/<int:pk>/editar/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/<int:pk>/eliminar/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # Paciente
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', PacienteDeleteView.as_view(), name='paciente_delete'),

    # Medico
    path('medicos/', MedicoListView.as_view(), name='medico_list'),
    path('medicos/nuevo/', MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/eliminar/', MedicoDeleteView.as_view(), name='medico_delete'),

    # Consulta
    path('consultas/', ConsultaListView.as_view(), name='consulta_list'),
    path('consultas/nuevo/', ConsultaCreateView.as_view(), name='consulta_create'),
    path('consultas/<int:pk>/editar/', ConsultaUpdateView.as_view(), name='consulta_update'),
    path('consultas/<int:pk>/eliminar/', ConsultaDeleteView.as_view(), name='consulta_delete'),

    # Tratamiento
    path('tratamientos/', TratamientoListView.as_view(), name='tratamiento_list'),
    path('tratamientos/nuevo/', TratamientoCreateView.as_view(), name='tratamiento_create'),
    path('tratamientos/<int:pk>/editar/', TratamientoUpdateView.as_view(), name='tratamiento_update'),
    path('tratamientos/<int:pk>/eliminar/', TratamientoDeleteView.as_view(), name='tratamiento_delete'),

    # Medicamento
    path('medicamentos/', MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/nuevo/', MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),

    # Receta
    path('recetas/', RecetaListView.as_view(), name='receta_list'),
    path('recetas/nuevo/', RecetaCreateView.as_view(), name='receta_create'),
    path('recetas/<int:pk>/editar/', RecetaUpdateView.as_view(), name='receta_update'),
    path('recetas/<int:pk>/eliminar/', RecetaDeleteView.as_view(), name='receta_delete'),
]
