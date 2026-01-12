#from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
    )

from .models import Prueba

from .forms import PruebaForm

class FoundationView (TemplateView):
    template_name='Home/home/foundation.html'
    
class IndexView (TemplateView):
    template_name='Home/home/home.html'
# Create your views here.

class PruebaListView(ListView):
    template_name='lista.html'
    queryset=['A','B','C']
    context_object_name='lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "pruebas.html"
    context_object_name='lita_prueba'



class PruebaCreateView(CreateView):
    template_name = "Home/home/add.html"
    model = Prueba
    form_class=PruebaForm
    success_url='/'

