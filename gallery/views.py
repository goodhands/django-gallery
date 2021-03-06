# Create your views here.
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Comment, Photo

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'recent_photos_list'

    def get_queryset(self):
        """
        Return the last five published photos
        Not including those set to be published in
        the future
        """
        return Photo.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:5]

class SingleView(generic.DetailView):
    model = Photo
    template_name = 'gallery/single.html'
    
    def get_queryset(self):
        """
        Excludes any photos that aren't published yet.
        """
        return Photo.objects.filter(created_at__lte=timezone.now())

class AuthorView(generic.DetailView):
    model = Photo
    template_name = 'gallery/author.html'

def comment(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    try:
        author = request.POST['author']
        comment = request.POST['comment']
    except KeyError:
        return render(request, 'gallery/single.html', {
            'photo': photo,
            'error_message': 'You must enter your name and comment'
        })
    else:
        c = Comment(author=author, comment=comment, photo=photo)
        c.save()

        return HttpResponseRedirect(reverse('gallery:show', args=(photo.id,)))