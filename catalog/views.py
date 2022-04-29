from django.shortcuts import render
from .models import PartList
from django.views.generic import TemplateView, ListView

# Create your views here.


class CatalogView(ListView):
    template_name = 'Catalog.html'
    model = PartList
    context_object_name = 'parts'

    