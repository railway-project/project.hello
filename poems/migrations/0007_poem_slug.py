# Generated by Django 4.2.2 on 2023-06-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0006_remove_poem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
