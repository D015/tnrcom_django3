# Generated by Django 3.2 on 2022-01-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
