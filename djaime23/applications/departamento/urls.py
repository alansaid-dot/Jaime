from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'lista/',
        views.DepartamentoListView.as_view(), 
        name='departamento-list'  # NOMBRE CORREGIDO
    ),
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='nuevo_departamento'
    ),
]