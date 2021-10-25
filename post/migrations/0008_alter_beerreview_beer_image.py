# Generated by Django 3.2.8 on 2021-10-25 13:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_beerreview_beer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerreview',
            name='beer_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
