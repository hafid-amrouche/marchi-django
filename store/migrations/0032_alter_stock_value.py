# Generated by Django 4.0.1 on 2022-06-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_alter_stock_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.ManyToManyField(to='store.Value'),
        ),
    ]
