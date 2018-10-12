from __future__ import unicode_literals

from django.db import models
from helloworld.settings import IMAGES_URL

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='static/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
