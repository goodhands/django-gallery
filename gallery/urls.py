from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'gallery'
urlpatterns = [
    # /gallery
    path('', views.index, name='index'),
    # /gallery/id
    path('<int:photo_id>/', views.show, name='show'),
    # /gallery/user/name
    path('user/<str:name>/', views.user, name='author'),
]