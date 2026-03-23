# File path utilities
from pathlib import Path

# Project ka root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Django ka secret key (production mein change karna zaroori hai)
SECRET_KEY = 'django-insecure-change-this-in-production-xyz123abc456'

# Debug mode - development mein ON, production mein OFF
DEBUG = True

# Kaunse domain names se requests accept karne hain
ALLOWED_HOSTS = ['*']

# Installed apps - Django aur hamara notes app
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',  # User authentication
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Flash messages
    'django.contrib.staticfiles',  # Static files (CSS, JS)
    'notes',  # Hamara notes app
]

# Middleware - security aur functionality ke liye
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security checks
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'django.middleware.common.CommonMiddleware',  # Common utilities
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # User authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# URL patterns ka root file
ROOT_URLCONF = 'sticky_project.urls'

# HTML templates ki settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Templates ka location
        'DIRS': [BASE_DIR / 'notes' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            # Context processors - templates mein data pass karne ke liye
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application - web server ke liye
WSGI_APPLICATION = 'sticky_project.wsgi.application'

# Database settings - SQLite use kar rahe hain
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file ka location
    }
}

# Password validation rules - strong passwords ensure karne ke liye
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # User ka naam jaise password nahi ho sakte
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Minimum 8 characters
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Common passwords block karo
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Sirf numbers wala password nahi
]

# Website ki language
LANGUAGE_CODE = 'en-us'
# Time zone
TIME_ZONE = 'UTC'
# Internationalization support
USE_I18N = True
# Timezone support
USE_TZ = True

# Static files ka URL (CSS, JS, images)
STATIC_URL = 'static/'
# Auto-generated field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout ke baad redirect karne ka URL
LOGIN_REDIRECT_URL = '/notes/'  # Login ke baad notes page par jao
LOGOUT_REDIRECT_URL = '/login/'  # Logout ke baad login page par jao
LOGIN_URL = '/login/'  # Default login page
