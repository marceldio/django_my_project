# Generated by Django 5.0.6 on 2024-08-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0013_product_is_published_product_view_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="slug"
            ),
        ),
    ]
