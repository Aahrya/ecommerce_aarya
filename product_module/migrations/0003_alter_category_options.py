# Generated by Django 4.0.6 on 2022-07-20 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_category_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]