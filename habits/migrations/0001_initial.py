# Generated by Django 5.1.4 on 2024-12-15 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                ("name", models.CharField(max_length=255)),
                ("place", models.CharField(max_length=255)),
                ("time", models.TimeField()),
                ("action", models.CharField(max_length=255)),
                ("is_pleasant", models.BooleanField(default=False)),
                ("reward", models.CharField(blank=True, max_length=255, null=True)),
                ("frequency", models.PositiveIntegerField(default=1)),
                (
                    "estimated_time",
                    models.PositiveIntegerField(help_text="Time in seconds"),
                ),
                ("is_public", models.BooleanField(default=False)),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_pleasant": True},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                    ),
                ),
            ],
        ),
    ]
