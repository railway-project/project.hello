# Generated by Django 4.2.2 on 2023-06-21 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0012_rename_content_comment_comment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
