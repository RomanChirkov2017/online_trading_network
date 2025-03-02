# Generated by Django 4.2 on 2024-07-11 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Element",
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
                    "title",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "item",
                    models.CharField(
                        choices=[
                            ("FACTORY", "Завод"),
                            ("RETAIL", "Розничная сеть"),
                            ("IE", "ИП"),
                        ],
                        max_length=50,
                        verbose_name="Тип элемента сети",
                    ),
                ),
                (
                    "level",
                    models.PositiveIntegerField(
                        choices=[("ZERO", "0"), ("ONE", "1"), ("TWO", "2")],
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "debt_to_supplier",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Долг перед поставщиком",
                    ),
                ),
                (
                    "date_of_creation",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        max_length=100,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="trading_network.element",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент сети",
                "verbose_name_plural": "Элементы сети",
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
                    "title",
                    models.CharField(max_length=150, verbose_name="Название продукта"),
                ),
                (
                    "model",
                    models.CharField(max_length=100, verbose_name="Модель продукта"),
                ),
                ("release_date", models.DateField(verbose_name="Дата выпуска")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading_network.element",
                        verbose_name="Элемент сети",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Contacts",
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
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Страна"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Улица"
                    ),
                ),
                (
                    "house",
                    models.CharField(
                        blank=True, max_length=5, null=True, verbose_name="Дом"
                    ),
                ),
                (
                    "unit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading_network.element",
                        verbose_name="Элемент сети",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
            },
        ),
    ]
