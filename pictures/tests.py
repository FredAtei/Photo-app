from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.travel = Category(name='travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category)) 

    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.Paris = Location(name='Paris')

    def test_instance(self):
        self.assertTrue(isinstance(self.Paris,Location)) 

    def test_save_method(self):
        self.Paris.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)       

class ImageTestClass(TestCase):
    def setUp(self):
        self.travel = Category(name = 'travel')
        self.travel.save_category()

        self.locations = Location(name='Paris')
        self.locations.save_location()

        self.new_image=Image(image_name='Eot',image_description='Great things',image_category=self.travel,image_location=self.locations)
        self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_get_images(self):
        all_images = Image.get_images()
        self.assertTrue(len(all_images)>0)

    def test_filter_by_location(self):
        test_location_id = 6
        images_location = Image.filter_by_location(test_location_id) 
        self.assertTrue(len(images_location) == 0)              