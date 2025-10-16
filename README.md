# Sistema de Gestión Clínica - Salud Vital

Sistema de gestión clínica desarrollado con Django y Django REST Framework para administrar pacientes, médicos, consultas, tratamientos y más.

---

## 📋 Requisitos previos

- Python 3.8 o superior
- PostgreSQL 12 o superior (opcional, puede usar SQLite para desarrollo)
- pip (gestor de paquetes de Python)

---

## 🚀 Paso a paso para configurar y ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/luisxdmaldonado1232-blip/eva2.git
cd eva2/start
```

### 2. Crear y activar un entorno virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**En Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install django djangorestframework django-filter psycopg2-binary drf-yasg
```

O si tienes un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

#### Opción A: Usar SQLite (desarrollo rápido)

Edita `drf/settings.py` y configura:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Opción B: Usar PostgreSQL (recomendado para producción)

1. **Crear la base de datos y usuario en PostgreSQL:**

Abre la consola de PostgreSQL (`psql`) como superusuario y ejecuta:

```sql
CREATE USER eva2_user WITH PASSWORD 'tu_password_seguro';
CREATE DATABASE eva2_db OWNER eva2_user;
GRANT ALL PRIVILEGES ON DATABASE eva2_db TO eva2_user;
```

2. **Editar `drf/settings.py`:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eva2_db',
        'USER': 'eva2_user',
        'PASSWORD': 'tu_password_seguro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Aplicar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario (opcional, para acceder al admin)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para definir usuario, email y contraseña.

### 7. Recopilar archivos estáticos (opcional, para producción)

```bash
python manage.py collectstatic
```

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000/**

---

## 🌐 Rutas principales

### Interfaces web (HTML/CRUD)
- **Inicio:** http://127.0.0.1:8000/web/
- **Pacientes:** http://127.0.0.1:8000/web/pacientes/
- **Médicos:** http://127.0.0.1:8000/web/medicos/
- **Consultas:** http://127.0.0.1:8000/web/consultas/
- **Tratamientos:** http://127.0.0.1:8000/web/tratamientos/
- **Medicamentos:** http://127.0.0.1:8000/web/medicamentos/
- **Recetas:** http://127.0.0.1:8000/web/recetas/
- **Especialidades:** http://127.0.0.1:8000/web/especialidades/

### API REST (JSON)
- **Endpoints:** http://127.0.0.1:8000/api/
  - `/api/pacientes/`
  - `/api/medicos/`
  - `/api/consultas/`
  - `/api/tratamientos/`
  - `/api/medicamentos/`
  - `/api/recetas/`
  - `/api/especialidades/`
  - `/api/seguros/`
  - `/api/horarios/`
  - `/api/citas/`
  - `/api/historiales/`

### Documentación de la API
- **Swagger UI:** http://127.0.0.1:8000/swagger/
- **Redoc:** http://127.0.0.1:8000/redoc/

### Panel de administración
- **Django Admin:** http://127.0.0.1:8000/admin/
- **DRF Auth:** http://127.0.0.1:8000/api-auth/

---

## 🛠️ Tecnologías utilizadas

- **Backend:** Django 5.x, Django REST Framework
- **Base de datos:** PostgreSQL / SQLite
- **Frontend:** Bootstrap 5
- **Documentación:** drf-yasg (Swagger/OpenAPI)
- **Filtros:** django-filter

---

## 📝 Notas adicionales

- Para usar filtros en la API, agrega parámetros de consulta:
  - Búsqueda: `/api/pacientes/?search=Juan`
  - Filtro: `/api/medicos/?especialidad=1&activo=true`
  
- El campo `fecha_nacimiento` en el formulario de pacientes usa un selector de calendario HTML5.

- Todos los templates incluyen un footer con nombre, sección y año.

---

## 👤 Autor

**Luis Maldonado** - Sección: AP-172-N4 - © 2025