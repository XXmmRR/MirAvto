from .views import CatalogView, CatalogDetailView, HomePageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', CatalogDetailView, name='details'),
]