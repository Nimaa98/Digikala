# Generated by Django 4.2.13 on 2024-06-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_icon_alter_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]
