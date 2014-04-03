from django.db import models
from django.contrib.auth.models import User

class Resources(models.Model):
    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"
        
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class Key(models.Model):
    class Meta:
        verbose_name = "Key"
        verbose_name_plural = "Keys"
        
    locks = models.ManyToManyField(Resources)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user
    
# Create your models here.
