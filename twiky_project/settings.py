from pathlib import Path
import os
from decouple import config 

# ✅ Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security settings
SECRET_KEY = config('SECRET_KEY', default='django-insecure-#sla7u9uuva*6v+4gt3)whx2mf74+fc715w8punbo24rmpzzjr')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,.vercel.app').split(',')


# ✅ Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twicky',  # Your app
]

# Add django_extensions only in development (not on Vercel)
if DEBUG and os.environ.get('VERCEL') != '1':
    INSTALLED_APPS.append('django_extensions')

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ URL configuration
ROOT_URLCONF = 'twiky_project.urls'

# ✅ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# ✅ WSGI Application
WSGI_APPLICATION = 'twiky_project.wsgi.application'

# ✅ Database - SQLite for Vercel (MongoDB causes issues with serverless)
# For production with MongoDB, use a different hosting service or containerized deployment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MongoDB connection (for future use with custom models)
MONGODB_URI = config('MONGODB_URI', default='mongodb+srv://Jitesh001:Jitesh001@twicky.fxotzly.mongodb.net/')

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static & Media Files Configuration
STATIC_URL = '/static/'

# Use /tmp for static files on Vercel (writable directory)
if os.environ.get('VERCEL'):
    STATIC_ROOT = '/tmp/staticfiles'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Create staticfiles directory only in non-Vercel environments
if not os.environ.get('VERCEL'):
    os.makedirs(STATIC_ROOT, exist_ok=True)

# Create static directory if it doesn't exist
STATICFILES_DIRS = []
static_dir = os.path.join(BASE_DIR, 'static')
if os.path.exists(static_dir):
    STATICFILES_DIRS = [static_dir]

# WhiteNoise configuration for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ✅ Media configuration for image uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ✅ Login URLs
LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/twicky/'
LOGOUT_REDIRECT_URL = '/twicky/'

# ✅ Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Security Settings for Production (Disabled for Vercel due to serverless)
# Note: Vercel handles HTTPS automatically
if not DEBUG and os.environ.get('VERCEL') != '1':
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
