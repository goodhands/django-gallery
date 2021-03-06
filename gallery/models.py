import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin

# Create your models here.
class Photo(models.Model):
    title = models.CharField('title', max_length=200, null=True)
    path = models.CharField('path', max_length=500, null=True)
    # name of the photographer, not the authed user
    name_of_creator = models.CharField('creator', max_length=200, null=True)
    date_taken = models.DateField('date taken', null=True)
    description = models.TextField('description', max_length=1000, null=True)
    update_at = models.DateField('updated date', null=True)
    created_at = models.DateField('created date', null=True)

    # Return string representation of this model 
    def __str__(self) -> str:
        return self.title

    def recent(self):
        year = timezone.now().year
        return Photo.objects.filter(created_at__year=year).order_by('-created_at')

    @admin.display(
        boolean=True,
        ordering='created_at',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return datetime.date(year=now.year, month=now.month, day=now.day) <= self.created_at <= now

class Comment(models.Model):
    author = models.CharField('author', max_length=100)
    comment = models.TextField('comment', max_length=1000)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    # Return string representation of this model 
    def __str__(self) -> str:
        return self.comment
