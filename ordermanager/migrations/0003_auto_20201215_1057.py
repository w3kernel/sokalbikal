# Generated by Django 3.1.1 on 2020-12-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0002_auto_20201215_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='min_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='promo',
            name='use_count',
            field=models.IntegerField(default=0),
        ),
    ]
