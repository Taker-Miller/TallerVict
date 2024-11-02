"""
Configuración de Django para el proyecto victoriaProyecto.

Generado por 'django-admin startproject' usando Django 4.2.6.

Para más información sobre este archivo, visita
https://docs.djangoproject.com/en/4.2/topics/settings/

Para ver la lista completa de configuraciones y sus valores, consulta
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Construcción de rutas internas del proyecto, como BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta de seguridad
SECRET_KEY = 'django-insecure-0ztr2#!vyvso79@vo+lg8($&%2*=y8(ad$saqa^mn6+y5tctxo'

# ¡ATENCIÓN! No ejecutes en producción con DEBUG activado
DEBUG = True

ALLOWED_HOSTS = []

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Archivos de medios (para contenido subido por el usuario)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion',  # Tu aplicación personalizada
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'victoriaProyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'gestion' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'victoriaProyecto.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es-es'  # Cambiado a español
TIME_ZONE = 'America/Santiago'  # Ajustado a la zona horaria de Chile
USE_I18N = True
USE_TZ = True

# Cierre de sesión automático después de 30 minutos de inactividad
SESSION_COOKIE_AGE = 1800  # 1800 segundos = 30 minutos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # La sesión expira al cerrar el navegador

# Tipo de campo predeterminado para la clave primaria
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
