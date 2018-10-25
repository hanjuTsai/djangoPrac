from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class PersonalDict(models.Model):
	DictName = models.CharField(max_length=20, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'pds')
	def __str__(self):
		return self.DictName