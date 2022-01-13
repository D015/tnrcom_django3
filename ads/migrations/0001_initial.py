# Generated by Django 3.2 on 2022-01-11 19:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False
                    ),
                ),
                ("time_create", models.DateTimeField(auto_now_add=True)),
                ("time_update", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                ("archived", models.BooleanField(default=False)),
                ("first_name", models.CharField(blank=True, max_length=150)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                ("date_of_birth", models.DateField(blank=True)),
                (
                    "photo",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
