from django.db import models
from cloudinary.models import CloudinaryField

class Picture(models.Model):
    image = CloudinaryField('image')

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length = 30)

class Category(models.Model):
    name = models.CharField(max_length = 30)

