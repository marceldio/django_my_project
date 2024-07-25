from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contact, card

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts', contact, name='contacts'),
    path('card', card, name='card')
]
