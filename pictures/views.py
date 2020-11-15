from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(locations)
    return render(request, 'pictures/index.html', {'images': images[::-1], 'locations':locations})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'pictures/index.html', {'location_images': images})    

def search_images(request):

    if 'photo' in request.GET and request.GET["photo"]:
        category= request.GET.get("photo")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'pictures/search_results.html',{"message":message, "photos":searched_images})

    else:
        message = "You have not searched for any picture"
        return render(request, 'pictures/search_results.html',{"message":message})    