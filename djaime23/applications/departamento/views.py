from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Departamento
from applications.personas.models import Empleado
from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'
    ordering = ['nombre']


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento-list')
    
    def get_context_data(self, **kwargs):
        """Añade departamentos existentes al contexto"""
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.all().order_by('nombre')
        return context

    def form_valid(self, form):
        """Procesa el formulario cuando es válido"""
        # Crear un departamento
        depa = Departamento(
            nombre=form.cleaned_data['departamento'],
            shorname=form.cleaned_data['shorname'],
            activo=True
        )
        depa.save()

        # Crear empleado administrador para el departamento
        Empleado.objects.create(
            first_name=form.cleaned_data['nombre'],
            last_name=form.cleaned_data['apellidos'],
            job='1',  # '1' = ADMINISTRADOR según tus choices en el modelo
            departamento=depa
        )
        return super().form_valid(form)