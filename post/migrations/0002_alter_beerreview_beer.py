# Generated by Django 3.2.8 on 2021-10-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerreview',
            name='beer',
            field=models.CharField(max_length=200),
        ),
    ]
