from django.db import models
from cloudinary.models import CloudinaryField

class Picture(models.Model):
    image = CloudinaryField('image')

class Image(models.Model):
    image=models.ImageField(upload_to = 'photos/')
    image_name=models.CharField(max_length =60)
    image_description=models.TextField()  

