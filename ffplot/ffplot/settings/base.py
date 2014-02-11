"""
Django settings for ffplot project.

base settings used in all versions
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

def create_project_root(*x):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
	
def add_to_project_root(*x):
	return os.path.join(os.path.abspath(PROJECT_ROOT), *x)
	
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = create_project_root("..", "..") # UNTESTED!!!

STATIC_ROOT = add_to_project_root("static") # UNTESTED!!!

TEMPLATE_DIRS = add_to_project_root("templates")

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'core',
    'playerdata',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ffplot.urls'

WSGI_APPLICATION = 'ffplot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'ffplotdb.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'