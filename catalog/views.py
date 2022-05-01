from django.shortcuts import render
from .models import PartList, Category, Part
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


def CatalogDetailView(request, slug):
    parts = PartList.objects.all()
    categories = Category.objects.filter(part_list__list_slug=slug)
    return render(request, 'Catalog_item_page.html', {'categories': categories, 'parts': parts})


def PartsListView(request, slug, category):
    parts_panel = PartList.objects.all()
    part = Part.objects.filter(category__category_slug=category, category__part_list__list_slug=slug)
    return render(request, 'add_cart.html', {'parts_main': part, 'parts': parts_panel})

# class PartsListView(ListView):
#     template_name = 'add_cart.html'
#     model = Part
#     context_object_name = 'parts'
#
#      def get_queryset(self, category):
#           return Part.object.filter(category__category_slug=category)

