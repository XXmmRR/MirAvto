from .views import CatalogView, CatalogDetailView, HomePageView, ContactPageView, PayPageView, DeliveryPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pay/', PayPageView.as_view(), name='pay_page'),
    path('delivery/', DeliveryPageView.as_view(), name='delivery'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', CatalogDetailView, name='details'),
]