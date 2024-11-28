from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listado/', views.LaboratorioListView.as_view(), name="laboratorios"),
]