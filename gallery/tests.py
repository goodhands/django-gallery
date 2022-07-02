import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Comment, Photo

def create_photo(title, dayAgo):
    """
    Create a photo with a given title and the dayAgo offset.
    Postive for future photos and negative for past photos
    """
    time = timezone.now() + datetime.timedelta(days=dayAgo)

    return Photo.objects.create(title=title, created_at=time)

class PhotoModelTests(TestCase):
    def test_no_photos(self):
        """
        If no photos exist, display the right message
        """
        response = self.client.get(reverse('gallery:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photos are available.")
        self.assertQuerysetEqual(response.context['recent_photos_list'], [])

    def test_past_photo(self):
        """
        If the photo was created in the past, it should show up
        """
        photo = create_photo("Welcome to the digital age", -100)
        response = self.client.get(reverse('gallery:index'))

        self.assertQuerysetEqual(response.context['recent_photos_list'], [photo])

    def test_future_photo(self):
        """
        If the future's date is a future date, it shouldn't show up
        """
        create_photo("The professor", 32)
        response = self.client.get(reverse('gallery:index'))

        self.assertContains(response, "No photos are available")
        self.assertQuerysetEqual(response.context['recent_photos_list'], [])

    def test_and_future_photos(self):
        """
        If there are future photos as well as past photos, only show the past photos
        """
        p_photo = create_photo("The night is long", -90)
        f_photo = create_photo("Flying cars", 180)

        response = self.client.get(reverse('gallery:index'))

        self.assertQuerysetEqual(response.context['recent_photos_list'], [p_photo])

    def test_multiple_photos_can_be_created(self):
        """
        We can publish more than 2 photos in the past and see them on the
        index page
        """
        first_photo = create_photo("Monalisa XXVII", -1)
        second_photo = create_photo("Monalisa XXXII", -1)

        response = self.client.get(reverse('gallery:index'))

        self.assertQuerysetEqual(response.context['recent_photos_list'], [first_photo, second_photo])
        self.assertEqual(response.status_code, 200)

    def test_was_published_recently_with_future_photo(self):
        """
        was_published_recently() returns False for photos whose created_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_photo = Photo(created_at=time)
        self.assertIs(future_photo.was_published_recently(), False)

    def test_photo_can_have_multiple_comments(self):
        """
        A photo should be able to have multiple comments attached in a list
        """

        photo = Photo(
                        title="A new time has come", 
                        path="a-new-time-has-come", 
                        name_of_creator="Sammy", 
                        description="A beautiful thing",
                        date_taken=datetime.date(2022, 7, 21)
                )
        photo.save()

        comment = Comment(author="Alariwo", comment="Yes indeed!", photo=photo)
        comment.save()

        self.assertEqual(len(photo.comment_set.all()), 1)

        comment_two = Comment(author="Alafia", comment="Alubarika", photo=photo)
        comment_two.save()

        self.assertEqual(len(photo.comment_set.all()), 2)

        self.assertIsInstance(comment.photo, Photo)