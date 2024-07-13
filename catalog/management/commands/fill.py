from django.core.management.base import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            categories = [item for item in data if item['model'] == 'catalog.category']
        return categories

    @staticmethod
    def json_read_products():
        with open('catalog.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            products = [item for item in data if item['model'] == 'catalog.product']
        return products

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_fields = category['fields']
            category_for_create.append(
                Category(
                    pk=category['pk'],
                    category=category_fields['category'],
                    description=category_fields['description'],
                    created_at=category_fields['created_at'],
                    updated_at=category_fields['updated_at']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_fields = product['fields']
            product_for_create.append(
                Product(
                    pk=product['pk'],
                    product=product_fields['product'],
                    description=product_fields['description'],
                    image=product_fields['image'],
                    category=Category.objects.get(pk=product_fields['category']),
                    price=product_fields['price'],
                    created_at=product_fields['created_at'],
                    updated_at=product_fields['updated_at']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
