from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listado/', views.LaboratorioListView.as_view(), name="laboratorios"),
    path('crea_lab/', views.LaboratorioCreateView.as_view(), name="crea_lab"),
    path('act_lab/<int:pk>', views.LaboratorioUpdateView.as_view(), name="act_lab"),
    path('del_lab/<int:pk>', views.LaboratorioDeleteView.as_view(), name="del_lab"),
    
    path('directores/', views.DirectorGeneralListView.as_view(), name="directores"),
    path('crea_dir/', views.DirectorGeneralCreateView.as_view(), name="crea_dir"),
    path('act_dir/<int:pk>', views.DirectorGeneralUpdateView.as_view(), name="act_dir"),
    path('del_dir/<int:pk>', views.DirectorGeneralDeleteView.as_view(), name="del_dir"),
    
    path('productos/', views.ProductoListView.as_view(), name="productos"),
    path('crea_prod/', views.ProductoCreateView.as_view(), name="crea_prod"),
    path('act_prod/<int:pk>', views.ProductoUpdateView.as_view(), name="act_prod"),
    path('del_prod/<int:pk>', views.ProductoDeleteView.as_view(), name="del_prod"),
]