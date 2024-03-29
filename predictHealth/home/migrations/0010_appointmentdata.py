# Generated by Django 5.0.2 on 2024-03-26 20:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_doctoruser"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AppointmentData",
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
                ("doctor", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=20)),
                ("appointmentDate", models.DateTimeField()),
                ("message", models.CharField(max_length=1000)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]