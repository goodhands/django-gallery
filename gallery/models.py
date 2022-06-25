import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField('title', max_length=200)
    path = models.CharField('path', max_length=500)
    # name of the photographer, not the authed user
    name_of_creator = models.CharField('creator', max_length=200)
    date_taken = models.DateTimeField('date taken')
    description = models.TextField('description', max_length=1000)
    update_at = models.DateTimeField('updated date', null=True)
    created_at = models.DateTimeField('created date', null=True)

    # Return string representation of this model 
    def __str__(self) -> str:
        return self.title

    def recent(self):
        year = timezone.now().year
        return Photo.objects.filter(created_at__year=year).order_by('-created_at')

class Comment(models.Model):
    author = models.CharField('author', max_length=100)
    comment = models.TextField('comment', max_length=1000)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)