from .views import CatalogView
from django.urls import path

urlpatterns = [
    path('', CatalogView.as_view()),
]