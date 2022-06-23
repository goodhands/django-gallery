# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Photo


def index(request):
    photo = Photo()
    
    recent_photos_list = photo.recent()[:5]

    context = {
        'recent_photos_list': recent_photos_list
    }

    return render(request, 'gallery/index.html', context)

def show(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'gallery/single.html', {'photo': photo})

def user(request, name):
    response = "You're looking at user %s photos"

    return HttpResponse(response % name)