# Generated by Django 3.1.1 on 2020-09-17 04:07

from django.db import migrations, models
import vendor.models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='shop_type',
            field=models.CharField(choices=[('virtual', 'Virtual'), ('existent', 'Existent ')], default='virtual', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='trade_licence',
            field=models.ImageField(blank=True, upload_to=vendor.models.upload_trade_path),
        ),
    ]