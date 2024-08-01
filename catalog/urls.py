from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contact, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),

    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='card'),
    path('contacts', contact, name='contacts'),
]
