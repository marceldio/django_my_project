from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # path('contacts', contact, name='contacts'),
]
