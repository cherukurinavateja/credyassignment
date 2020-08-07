import uuid
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from movielist.models import MovieLists


class Moviecollections(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100, default= "")
	description = models.TextField(default="")
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	movies = models.ManyToManyField(MovieLists)

	def __str__(self):
		return self.title
