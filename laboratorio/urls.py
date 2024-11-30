from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listado/', views.LaboratorioListView.as_view(), name="laboratorios"),
    path('crea_lab/', views.LaboratorioCreateView.as_view(), name="crea_lab"),
    path('act_lab/<int:pk>', views.LaboratorioUpdateView.as_view(), name="act_lab"),
    path('del_lab/<int:pk>', views.LaboratorioDeleteView.as_view(), name="del_lab"),
]