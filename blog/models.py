from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="Слаг",
        help_text="Слаг для создания уникальной ссылки",
        unique=True,
    )
    content = models.TextField(
        verbose_name="Содержание",
        help_text="Введите текст",
    )
    image = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
        help_text="Количество просмотров")
    slug = models.CharField(max_length=450,
                            verbose_name= 'slug', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]
