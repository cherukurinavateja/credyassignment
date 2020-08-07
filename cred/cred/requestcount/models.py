from django.db import models

# Create your models here.

class UserRequest(models.Model):
	requests = models.IntegerField()
