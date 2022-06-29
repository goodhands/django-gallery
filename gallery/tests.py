import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Photo


class PhotoModelTests(TestCase):

    def test_was_published_recently_with_future_photo(self):
        """
        was_published_recently() returns False for photos whose created_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_photo = Photo(created_at=time)
        self.assertIs(future_photo.was_published_recently(), False)