from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contact, card

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),

    path('catalog/<int:pk>/', card, name='card'),
    path('contacts', contact, name='contacts'),
]
