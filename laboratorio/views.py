from django.shortcuts import render
from .models import Laboratorio
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LaboratorioForm
# from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# from django.shortcuts import redirect
#from .forms import LaboratorioForm
# from django.contrib.auth.decorators import login_required, permission_required 
# from django.forms import ValidationError
# from django.contrib import messages

#Estas Importaciones son para la vista basada en funciones
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = "laboratorio/laboratorios.html"
    form_class = LaboratorioForm
    context_object_name="laboratorios"


#Vista basada en Clases para Creacion de Laboratorios

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = "laboratorio/crea_lab.html"
    #fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = "laboratorio/act_lab.html"
    #fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = "laboratorio/del_lab.html"
    success_url = reverse_lazy('laboratorios')

