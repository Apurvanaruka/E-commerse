# Generated by Django 4.2.1 on 2023-05-27 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='iamge',
            new_name='image',
        ),
    ]
