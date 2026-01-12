from pathlib import Path
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = [
    'jaime-sfhm.onrender.com',
    'localhost',
    '127.0.0.1',
]



ROOT_URLCONF = 'empleado.urls'



DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR.parent / 'static']

MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_ROOT = BASE_DIR / 'media'