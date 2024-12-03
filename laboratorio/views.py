from django.shortcuts import render
from .models import Laboratorio, DirectorGeneral, Producto
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm

#Estas Importaciones son para la vista basada en funciones
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = "laboratorio/laboratorios.html"
    form_class = LaboratorioForm
    context_object_name="laboratorios"


###############################################################
#           Aqui comienzan las vistas de Laboratorios         #
###############################################################

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = "laboratorio/act_crea_lab.html"
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = "laboratorio/act_crea_lab.html"
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = "laboratorio/del_lab.html"
    success_url = reverse_lazy('laboratorios')

###############################################################
#           Aqui comienzan las vistas de Directores           #
###############################################################

class DirectorGeneralListView(ListView):
    model = DirectorGeneral
    template_name = "directores/directores.html"
    form_class = DirectorGeneralForm
    context_object_name="directores"

class DirectorGeneralCreateView(CreateView):
    model = DirectorGeneral
    form_class = DirectorGeneralForm
    template_name = "directores/act_crea_direct.html"
    success_url = reverse_lazy('directores')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    
class DirectorGeneralUpdateView(UpdateView):
    model = DirectorGeneral
    form_class = DirectorGeneralForm
    template_name = "directores/act_dir.html"
    success_url = reverse_lazy('directores')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class DirectorGeneralDeleteView(DeleteView):
    model = DirectorGeneral
    template_name = "directores/del_dir.html"
    success_url = reverse_lazy('directores')
    
###############################################################
#           Aqui comienzan las vistas de productos            #
###############################################################
    
class ProductoListView(ListView):
    model = Producto
    template_name = "productos/productos.html"
    form_class = ProductoForm
    context_object_name="productos"

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crea_prod.html"
    success_url = reverse_lazy('productos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/act_prod.html"
    success_url = reverse_lazy('productos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/del_prod.html"
    success_url = reverse_lazy('productos')