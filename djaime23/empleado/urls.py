"""
URL configuration for empleado project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # EL ORDEN IMPORTA: personas primero porque tiene path ''
    path('', include('applications.personas.urls')),
    # departamento con prefijo para evitar conflictos
    path('departamento/', include('applications.departamento.urls')),
    # home al final
    path('', include('applications.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)