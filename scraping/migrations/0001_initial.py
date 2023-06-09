# Generated by Django 4.2 on 2023-05-09 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseScraping",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=254)),
                ("description", models.CharField(max_length=254)),
                ("price", models.DecimalField(decimal_places=2, max_digits=13)),
                ("rating", models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                "db_table": "BaseScraping",
            },
        ),
        migrations.CreateModel(
            name="KeyWord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=254, null=True)),
                ("date", models.DateField()),
            ],
            options={
                "db_table": "Keyword",
            },
        ),
        migrations.CreateModel(
            name="Organic",
            fields=[
                (
                    "basescraping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="scraping.basescraping",
                    ),
                ),
            ],
            options={
                "db_table": "Organic",
            },
            bases=("scraping.basescraping",),
        ),
        migrations.CreateModel(
            name="Sponsored",
            fields=[
                (
                    "basescraping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="scraping.basescraping",
                    ),
                ),
            ],
            options={
                "db_table": "Sponsored",
            },
            bases=("scraping.basescraping",),
        ),
    ]
