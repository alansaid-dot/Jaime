from django.urls import path
from . import views 

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-todos-empleados/', views.LisAllEmpleados.as_view(), name='empleados_all'),
    path('list-by-area/<subnombre>/', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('lista-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('buscar-empleado/', views.ListEmpleadoBykword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmplado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleados_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]