# Generated by Django 3.1.1 on 2020-09-15 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='vendor',
        ),
    ]
