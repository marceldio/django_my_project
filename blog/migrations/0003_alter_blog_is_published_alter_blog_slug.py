# Generated by Django 5.0.6 on 2024-08-04 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.CharField(max_length=450, verbose_name="slug"),
        ),
    ]
