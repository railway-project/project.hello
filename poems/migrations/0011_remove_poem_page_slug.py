# Generated by Django 4.2.2 on 2023-06-21 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0010_poem_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='page_slug',
        ),
    ]