from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) 

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def filter_by_location(cls,id):
        image_by_location = cls.objects.filter(image_location_id = id)  
        return image_by_location

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category)
        return images

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()     

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations    

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

