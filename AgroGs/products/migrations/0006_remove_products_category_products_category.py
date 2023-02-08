# Generated by Django 4.1.2 on 2023-02-08 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_remove_products_image_products_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="category",
        ),
        migrations.AddField(
            model_name="products",
            name="category",
            field=models.ForeignKey(
                default=0.0004531224254407645,
                on_delete=django.db.models.deletion.PROTECT,
                to="products.category",
                verbose_name="Category",
            ),
            preserve_default=False,
        ),
    ]
