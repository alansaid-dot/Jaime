from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('foundation/', views.FoundationView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('pruebas_lista/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
]