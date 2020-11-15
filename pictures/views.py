from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(locations)
    return render(request, 'pictures/index.html', {'images': images[::-1], 'locations':locations})

def photos_by_location(request, location_id):
    images = Image.filter_by_location(location_id) 
    return render(request,'all-photos/index.html',{"images":images})    