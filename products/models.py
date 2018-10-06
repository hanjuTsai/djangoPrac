from django.db import models
from django.conf import settings

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length = 100,blank = False)
    link = models.CharField(max_length = 100,blank = False)
    size = models.IntegerField(blank=False)
    filetype = models.CharField(max_length = 5, blank = False)
    deletehash = models.CharField(max_length = 100,blank = False)

    def __str__(self) :
        return self.title
