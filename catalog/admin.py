from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
