# Log de Desarrollo - Movie Reviews Project

## Resumen del Proyecto
Proyecto Django para reseñas de películas desarrollado paso a paso.

## Problemas Encontrados y Soluciones

### 1. Error en URLs (Primer problema)
**Error:** `NameError: name 'movieViews' is not defined`
**Causa:** En `moviereviews/urls.py` se importó como `movie_views` pero se usó `movieViews`
**Solución:** Cambiar `movieViews.home` por `movie_views.home`

```python
# Antes (Error)
from movie import views as movie_views
path('', movieViews.home),

# Después (Correcto)
from movie import views as movie_views
path('', movie_views.home),
```

### 2. Creación de .gitignore
**Problema:** No existía archivo .gitignore
**Solución:** Creado `.gitignore` con configuraciones para proyectos Django incluyendo:
- `__pycache__/`
- `*.pyc`
- `db.sqlite3`
- `.env`
- `venv/`
- `.vscode/`
- `media/`
- `staticfiles/`

### 3. Problema con Git Add
**Error:** `fatal: pathspec 'about.html' did not match any files`
**Causa:** Se intentó usar `git add about.html` en lugar de la ruta completa
**Solución:** Usar `git add movie\templates\about.html` (ruta completa)

### 4. Error en Settings.py
**Error:** `Media_ROOT` (mayúsculas incorrectas)
**Solución:** Cambiar a `MEDIA_ROOT` (todo en mayúsculas)

```python
# Antes (Error)
Media_ROOT = os.path.join(BASE_DIR, 'media')

# Después (Correcto)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 5. Error en Admin.py
**Error:** `ModuleNotFoundError: No module named 'models'`
**Causa:** Import incorrecto en `movie/admin.py`
**Solución:** Cambiar import absoluto por import relativo

```python
# Antes (Error)
from models import Movie

# Después (Correcto)
from .models import Movie
```

### 6. Migraciones
**Proceso:** 
1. `python manage.py makemigrations` - Crear migraciones
2. `python manage.py migrate` - Aplicar migraciones
**Estado:** Todas las migraciones aplicadas correctamente

## Estructura Final del Proyecto

```
moviereviewsproject/
├── .gitignore
├── requirements.txt
├── db.sqlite3
├── manage.py
├── movie/
│   ├── __init__.py
│   ├── admin.py          # Registra modelo Movie
│   ├── apps.py
│   ├── models.py         # Modelo Movie con ImageField
│   ├── tests.py
│   ├── views.py          # Vista home
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── templates/
│       ├── home.html     # Template principal
│       └── about.html    # Template about (vacío)
└── moviereviews/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py       # Configuración con MEDIA_ROOT
    ├── urls.py           # URLs principales
    └── wsgi.py
```

## Modelo Movie

```python
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='movies/imagenes/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
```

## Dependencias (requirements.txt)

```
asgiref==3.8.1
Django==5.2.1
pillow==11.3.0
sqlparse==0.5.3
tzdata==2025.2
```

## Comandos Útiles Utilizados

### Git
- `git status` - Ver estado del repositorio
- `git add movie\templates\about.html` - Agregar archivo específico
- `git add .` - Agregar todos los archivos

### Django
- `python manage.py makemigrations` - Crear migraciones
- `python manage.py migrate` - Aplicar migraciones
- `python manage.py runserver` - Ejecutar servidor
- `python manage.py showmigrations` - Ver estado de migraciones

### Python/Pip
- `pip freeze > requirements.txt` - Generar requirements
- `pip install -r requirements.txt` - Instalar dependencias

## Comentarios en Python
Para comentar una línea en Python se usa `#`:
```python
# Esta línea está comentada
return render(request, 'home.html')  # Comentario al final de línea
```

## Atajos de VS Code
- `Ctrl + /` - Comentar/descomentar líneas seleccionadas

## Estado Final
✅ Servidor funcionando en `http://127.0.0.1:8000/`
✅ Panel admin disponible en `http://127.0.0.1:8000/admin/`
✅ Modelo Movie registrado en admin
✅ Templates configurados
✅ Archivos de configuración creados (.gitignore, requirements.txt)

## Rama de Desarrollo
- Repositorio: `taller_1_P1`
- Owner: `ssabogall`
- Rama actual: `main`

---
*Documentación generada el 31 de julio de 2025*
