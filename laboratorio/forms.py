from django import forms
from .models import Laboratorio, DirectorGeneral

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        widgets = {
            #'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del laboratorio'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DirectorGeneralForm(forms.ModelForm):
    
    class Meta:
        model = DirectorGeneral
        fields = ["nombre", "laboratorio", "especialidad"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
