# Generated by Django 4.0.1 on 2022-07-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_rename_images_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(max_length=255, upload_to='stores/products/'),
        ),
    ]
