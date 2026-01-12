from pathlib import Path
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.parent / 'static']

MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_ROOT = BASE_DIR / 'media'