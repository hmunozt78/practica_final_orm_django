from django.shortcuts import render
from .models import Laboratorio
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# from django.shortcuts import redirect
#from .forms import LaboratorioForm
# from django.contrib.auth.decorators import login_required, permission_required 
# from django.forms import ValidationError
# from django.contrib import messages

# Create your views here.

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = "laboratorio/laboratorios.html"
    context_object_name="laboratorios"


class LaboratorioCreateView(CreateView):
    model = Laboratorio
    template_name = "laboratorio/crea_lab.html"
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    template_name = "laboratorio/act_lab.html"
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = "laboratorio/del_lab.html"
    success_url = reverse_lazy('laboratorios')

