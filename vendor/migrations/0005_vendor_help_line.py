# Generated by Django 3.1.1 on 2020-09-17 04:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_auto_20200917_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='help_line',
            field=models.CharField(blank=True, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number'),
        ),
    ]
