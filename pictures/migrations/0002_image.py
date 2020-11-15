# Generated by Django 3.1.3 on 2020-11-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('image_name', models.CharField(max_length=60)),
                ('image_description', models.TextField()),
            ],
        ),
    ]