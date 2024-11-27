from django.db import models

# Create your models here.

class Laboratorio(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)

    class Meta:
        managed = True
        db_table = 'laboratorios'
        
class DirectorGeneral(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
    laboratorio = models.OneToOneField(Laboratorio,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'directores_generales'
        

class Producto(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False,unique=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, null=False, blank=False)
    f_fabricacion = models.DateField(blank=False, null=False)
    p_costo = models.FloatField()
    p_costo = models.FloatField()

    class Meta:
        managed = True
        db_table = 'productos'