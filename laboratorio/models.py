from django.db import models

# Create your models here.


class Laboratorio(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
    ciudad = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'laboratorios'
        
        
class DirectorGeneral(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
    laboratorio = models.OneToOneField(Laboratorio,on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'directores_generales'
        

class Producto(models.Model):

    fechas_choices = [
         (anio, str(anio)) for anio in range(2015, 2025)
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, null=False, blank=False)
    f_fabricacion = models.IntegerField(choices=fechas_choices, default=2024, verbose_name='F Fabricación')
    p_costo = models.DecimalField(null=False, blank=False, default=0, max_digits=12,decimal_places=2)
    p_venta = models.DecimalField(null=False, blank=False, default=0, max_digits=12,decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'productos'