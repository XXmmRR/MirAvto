from django.shortcuts import render
from .models import PartList, Category
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.


class HomePageView(ListView):
    template_name = 'HomePage.html'
    model = PartList
    context_object_name = 'parts'


class FeedBackPageView(ListView):
    template_name = 'CallBackPage.html'
    model = PartList
    context_object_name = 'parts'


class DeliveryPageView(ListView):
    template_name = 'deliveryPage.html'
    model = PartList
    context_object_name = 'parts'


class PayPageView(ListView):
    template_name = 'PayPage.html'
    model = PartList
    context_object_name = 'parts'


class ContactPageView(ListView):
    template_name = 'Contact.html'
    model = PartList
    context_object_name = 'parts'


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
