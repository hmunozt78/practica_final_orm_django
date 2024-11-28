from django.shortcuts import render
from .models import Laboratorio
from django.views.generic import ListView
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
