# Generated by Django 4.2.2 on 2023-06-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0014_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]