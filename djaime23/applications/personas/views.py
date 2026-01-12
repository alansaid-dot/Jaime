from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#models
from .models import Empleado
# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga página de inicio """
    template_name = 'inicio.html'

class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by= 7
    ordering='first_name'  # CORREGIDO
    context_object_name='empleados'
    model=Empleado


class LisAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by= 7
    ordering='first_name'  # CORREGIDO
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
            )
        return lista

class ListByAreaEmpleado(ListView):
    """Lista empleados de un area"""
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
   

    def get_queryset(self):
       area=self.kwargs['subnombre']
       lista=Empleado.objects.filter(
           departamento__subnombre=area
       )   
       return lista

class ListEmpleadoBykword(ListView):
    """Lista de empleado por palabra clave"""
    template_name='persona/by_kword.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        print('*************************')
        palabra_clave=self.request.GET.get("kword",'')
        #print('=================',palabra_clave)
        lista=Empleado.objects.filter(first_name=palabra_clave)  # CORREGIDO
        return lista
    
class ListHabilidadesEmplado(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=1)
        return empleado.habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url=reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name  # CORREGIDO
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUdateView(UpdateView):
    template_name="persona/update.html"
    model= Empleado
    fields=[
        'first_name',  # CORREGIDO
        'last_name',
        'full_name',
        'job', 
        'departamento',
        'habilidades'
        ]
    success_url=reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('#############METODO POST ###################3')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        print('****metodo form valid *******')
        self.object = form.save()
        return super(EmpleadoUdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name="persona/delete.html"
    success_url=reverse_lazy('persona_app:empleados_admin')