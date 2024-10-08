# Generated by Django 5.0.6 on 2024-07-11 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        help_text="Введите дату записи в БД",
                        verbose_name="Дата записи в БД",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        help_text="Введите дату обновления записи в БД",
                        verbose_name="Дата обновления записи в БД",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["category", "description"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.CharField(
                        help_text="Введите наименование товара",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание товара", verbose_name="Описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение товара",
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="Введите цену за покупку  товара",
                        verbose_name="Цена за покупку",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        help_text="Введите дату записи в БД",
                        verbose_name="Дата записи в БД",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        help_text="Введите дату обновления записи в БД",
                        verbose_name="Дата обновления записи в БД",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию товара",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["product", "description", "category", "price"],
            },
        ),
    ]
