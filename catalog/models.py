from django.db import models


class Category(models.Model):
    category = models.CharField(
        max_length=100,
        verbose_name="Категория"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category", "description"]

    def __str__(self):
        return self.category


class Product(models.Model):
    product = models.CharField(
        max_length=100,
        verbose_name="Наименование"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    slug = models.CharField(
        max_length=200,
        verbose_name='slug',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="products"
    )
    price = models.PositiveIntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
        editable=False
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product", "description", "category", "price"]

    def __str__(self):
        return f'{self.product}'


class Version(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    number = models.PositiveIntegerField(verbose_name='номер версии')
    is_current = models.BooleanField(default=True, verbose_name='активная')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
