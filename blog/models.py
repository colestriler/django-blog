from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
	title = models.CharField(max_length=200, default="TITLE")
	description = models.CharField(max_length=300, default="DESCRIPTION")
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_year(self):
		return self.date.year

	def __str__(self):
		return self.title

class BookReview(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=40)
	review = models.TextField()
	rating = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.review