import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Comment, Photo


class PhotoModelTests(TestCase):

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