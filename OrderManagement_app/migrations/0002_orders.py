# Generated by Django 4.2.17 on 2024-12-11 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invent_app", "0002_products_is_food_product"),
        ("OrderManagement_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("order_number", models.CharField(max_length=10, null=True)),
                ("order_date", models.DateField(null=True)),
                ("quantity", models.FloatField(default=0)),
                ("amount", models.FloatField(default=0)),
                ("gst_amount", models.FloatField(default=0)),
                ("bill_amount", models.FloatField(default=0)),
                (
                    "customer_reference",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="OrderManagement_app.customer",
                    ),
                ),
                (
                    "product_reference",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="invent_app.products",
                    ),
                ),
            ],
        ),
    ]