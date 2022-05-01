from .views import CatalogView, CatalogDetailView, HomePageView, ContactPageView, PayPageView, DeliveryPageView, \
    FeedBackPageView, PartsListView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('feedback/', FeedBackPageView.as_view(), name='feedback'),
    path('pay/', PayPageView.as_view(), name='pay_page'),
    path('delivery/', DeliveryPageView.as_view(), name='delivery'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', CatalogDetailView, name='details'),
    path('catalog/<slug:slug>/<slug:category>/', PartsListView, name='cart'),
]
