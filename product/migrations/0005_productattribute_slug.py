# Generated by Django 3.1.1 on 2020-09-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200916_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]