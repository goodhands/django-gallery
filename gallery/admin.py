from django.contrib import admin
from .models import Comment, Photo

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 4

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About the photo',  {'fields': ['title', 'path', 'description', 'date_taken']}),
        ('About the owner',  {'fields': ['name_of_creator']}),
        ('Other information', {'fields': ['created_at', 'update_at']})
    ]
    inlines = [CommentInline]
    list_display = ('title', 'name_of_creator', 'date_taken', 'was_published_recently')
    list_filter = ['created_at', 'name_of_creator']
    search_fields = ['description']

admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Comment)
# Register your models here.
