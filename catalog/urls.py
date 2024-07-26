from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contact, card

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('contacts', contact, name='contacts'),
    path('card', card, name='card')
]
