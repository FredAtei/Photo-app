# Generated by Django 3.1.3 on 2020-11-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20201115_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]