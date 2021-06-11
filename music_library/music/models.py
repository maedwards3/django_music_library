from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=75)
    artist = models.CharField(max_length=75)
    album = models.CharField(max_length=75)
    release_date = models.DateTimeField()
