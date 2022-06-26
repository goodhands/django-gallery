from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    # /gallery
    path('', views.IndexView.as_view(), name='index'),
    # /gallery/id
    path('<int:pk>/', views.SingleView.as_view(), name='show'),
    # /gallery/id/comment
    path('<int:photo_id>/comment', views.comment, name='comment'),
    # /gallery/user/name
    path('user/<str:name>/', views.AuthorView.as_view(), name='author'),
]