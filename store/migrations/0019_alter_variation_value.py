# Generated by Django 4.0.3 on 2022-03-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_value_variation_variation_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='value',
            field=models.ManyToManyField(to='store.value'),
        ),
    ]
