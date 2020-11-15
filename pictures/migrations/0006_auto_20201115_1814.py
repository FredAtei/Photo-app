# Generated by Django 3.1.3 on 2020-11-15 15:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0005_auto_20201115_1739'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
