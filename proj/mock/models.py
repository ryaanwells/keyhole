from django.db import models

# Create your models here.
class Pictures(models.Model):
    pic = models.CharField(max_length=128, null=True, blank=True)

class Audio(models.Model):
    audio = models.CharField(max_length=128, null=True, blank=True)

class Feed(models.Model):
    feed = models.CharField(max_length=128, null=True, blank=True)
