# Generated by Django 4.0.3 on 2022-03-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_product_off_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='off_price',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
