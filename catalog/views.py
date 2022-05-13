from django.shortcuts import render, redirect
from .models import PartList, Category, Product, Mark
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.


class HomePageView(ListView):
    template_name = 'HomePage.html'
    model = PartList
    extra_context = {'marks': Mark.objects.all()}
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
    get_object_or_404(PartList, list_slug=slug)
    return render(request, 'Catalog_item_page.html', {'categories': categories, 'parts': parts})


def PartsListView(request, slug, category):
    parts_panel = PartList.objects.all()
    part = Product.objects.filter(category__category_slug=category, category__part_list__list_slug=slug)
    return render(request, 'add_cart.html', {'parts_main': part, 'parts': parts_panel})


class PartSearchListView(ListView):
    model = PartList
    context_object_name = 'parts'
    template_name = 'Catalog.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return PartList.objects.filter(
            Q(mark__icontains=query)
        )


class DetailSearchView(ListView):
    model = Product
    context_object_name = 'parts_main'
    parts_panel = PartList.objects.all()
    extra_context = {'parts': parts_panel}
    template_name = 'add_cart.html'

    def get_queryset(self):
        query = self.request.GET.get('g')
        return Product.objects.filter(
            Q(article__icontains=query) |
            Q(article_second__icontains=query) |
            Q(part_name__icontains=query)
        )


class CartPageView(TemplateView):
    template_name = "basket.html"


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("basket")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("basket")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("basket")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("basket")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("basket")


@login_required
def payment(request):
    return HttpResponse("Вы провели оплату")
