# Generated by Django 3.1.13 on 2022-04-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="banner_art",
            field=models.ImageField(null=True, upload_to="images"),
        ),
    ]
