# Generated by Django 3.1.1 on 2020-12-08 05:45

from django.db import migrations
import image_optimizer.fields
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200917_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to=product.models.upload_image_path),
        ),
    ]