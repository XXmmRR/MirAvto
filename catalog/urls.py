from .views import CatalogView, CatalogDetailView
from django.urls import path

urlpatterns = [
    path('catalog/', CatalogView.as_view()),
    path('catalog/<slug:slug>/', CatalogDetailView, name='details')
]