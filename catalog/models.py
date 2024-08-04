from django.db import models


class Category(models.Model):
    category = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание категории",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата записи в БД", help_text="Введите дату записи в БД"
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления записи в БД",
        help_text="Введите дату обновления записи в БД",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category", "description"]

    def __str__(self):
        return self.category


class Product(models.Model):
    product = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    # photo = models.ImageField(
    #     upload_to="catalog/photo",
    #     blank=True,
    #     null=True,
    #     verbose_name="Изображение",
    #     help_text="Загрузите изображение",
    # )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку  товара"
    )
    # created_at = models.DateTimeField(
    #     verbose_name="Дата записи в БД", help_text="Введите дату записи в БД"
    # )
    # updated_at = models.DateTimeField(
    #     verbose_name="Дата обновления записи в БД",
    #     help_text="Введите дату обновления записи в БД"
    # )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
        help_text="Количество просмотров")


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product", "description", "category", "price"]

    def __str__(self):
        return self.product
