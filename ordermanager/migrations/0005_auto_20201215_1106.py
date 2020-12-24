# Generated by Django 3.1.1 on 2020-12-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0004_auto_20201215_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('payment pending', 'Payment Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='created', max_length=15),
        ),
    ]
