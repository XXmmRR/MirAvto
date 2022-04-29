from django.shortcuts import render
from .models import PartList, Category
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'HomePage.html'


class PayPageView(TemplateView):
    template_name = 'PayPage.html'


class ContactPageView(TemplateView):
    template_name = 'Contact.html'


class CatalogView(ListView):
    template_name = 'Catalog.html'
    model = PartList
    context_object_name = 'parts'

# class CatalogDetailView(ListView):
#      template_name = 'Catalog_item_page.html'
#      model = Category
#      context_object_name = 'categories'
#


def CatalogDetailView(request, slug):
    categories = Category.objects.filter(part_list__list_slug=slug)
    return render(request, 'Catalog_item_page.html', {'categories': categories} )
