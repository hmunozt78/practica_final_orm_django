# from django.shortcuts import render

# def index(request):
#     contexto = {}
#     return render(request, 'index.html', contexto)

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'