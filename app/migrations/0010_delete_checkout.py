# Generated by Django 4.2.1 on 2023-06-01 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_order_total'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
