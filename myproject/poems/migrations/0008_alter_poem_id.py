# Generated by Django 4.2.2 on 2023-06-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0007_poem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
