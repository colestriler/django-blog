import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Post

class PostModelTests(TestCase):
	def test_get_year(self):
		"""
		was_published_recently() returns False for questions
		whose pub_date is in the future
		"""
		date = timezone.now()
		post = Post(date=date)
		self.assertEquals(post.get_year(), 2019)