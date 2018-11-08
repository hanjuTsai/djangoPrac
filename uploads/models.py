from __future__ import unicode_literals
import os
import uuid

from django.db import models
from helloworld.settings import IMAGES_URL
from django.dispatch import receiver

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

@ receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.document:
        if os.path.isfile(instance.document.path):
            os.remove(instance.document.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):

    if not instance.pk:
        return False
    try:
        old_file = Document.objects.get(pk=instance.pk).document
    except Document.DoesNotExist:
        return False

    new_file = instance.document
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)