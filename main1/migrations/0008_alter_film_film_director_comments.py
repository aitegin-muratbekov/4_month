# Generated by Django 4.1.2 on 2022-10-24 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main1", "0007_alter_film_film_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="film",
            name="film_director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main1.director",
            ),
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("name", models.CharField(max_length=200)),
                ("comm", models.TextField(max_length=1000)),
                (
                    "film",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main1.film",
                    ),
                ),
            ],
        ),
    ]