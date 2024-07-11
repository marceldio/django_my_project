from django.urls import path
# from catalog.apps import NewappConfig
# app_name = NewappConfig.name
from catalog.apps import CatalogConfig
from catalog.views import index, contact

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),

    path('contacts', contact, name='contacts')
]
