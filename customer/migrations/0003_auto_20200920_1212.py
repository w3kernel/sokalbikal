# Generated by Django 3.1.1 on 2020-09-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
    ]
