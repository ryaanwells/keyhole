from django.db import models
from django.contrib.auth.models import User

class Methods(models.Model):
    class Meta:
        verbose_name = "Method"
        verbose_name_plural = "Methods"

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Resources(models.Model):
    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"
        
    methods = (
        ('G', 'GET'),
        ('P', 'POST'),
        ('A', 'PATCH'),
        ('U', 'PUT'),
        ('D', 'DELETE'),
    )

    name = models.CharField(max_length=128)
    allowed_methods = models.ManyToManyField(Methods)

    def __unicode__(self):
        return self.name

class Key(models.Model):
    class Meta:
        verbose_name = "Key"
        verbose_name_plural = "Keys"
        
    user = models.ForeignKey(User)
    locks = models.ForeignKey(Resources, null=True)
    allowed_methods = models.ManyToManyField(Methods)


    def save(self, *args, **kwargs):
        if self.pk is not None:
            for m in self.allowed_methods.all():
                if m not in self.locks.allowed_methods.all():
                    self.allowed_methods.remove(m)
        super(Key, self).save()

    def __unicode__(self):
        return "hello" #self.user.username #"{} - {}".format(self.user.username, self.locks.name)
    

