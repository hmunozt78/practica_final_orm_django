from django import forms
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }
 
class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el nombre del director general'
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Especialidad del director (opcional)'
            }),
            'laboratorio': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].queryset = Laboratorio.objects.filter(directorgeneral__isnull=True)
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'laboratorio': forms.Select(attrs={
                'class': 'form-select'
            }),
            'f_fabricacion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'p_costo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio de costo'
            }),
            'p_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio de venta'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].queryset = Laboratorio.objects.all()

