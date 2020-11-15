from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^location/', views.image_location, name='Location'),
    url(r'^search/', views.searched_images, name = 'search_images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)