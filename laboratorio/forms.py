from django import forms

from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    
    class Meta:
        model = Laboratorio
        fields = ("nombre","ciudad","pais",)

# id = models.AutoField(primary_key=True)
# nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
# ciudad = models.CharField(max_length=100, null=False, blank=False, default='Santiago')
# pais = models.CharField(max_length=100, null=False, blank=False, default='Chile')

