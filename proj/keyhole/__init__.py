from django.conf import settings
import os, sys, inspect
from itertools import chain
from importlib import import_module
from tastypie.resources import ModelResource
from models import Resources

if hasattr(settings, "KEYHOLsE"):
    for res in settings.KEYHOLE["resources"]:
        imports = import_module(res)
        for name, obj in inspect.getmembers(imports):
            if inspect.isclass(obj) and issubclass(obj, ModelResource) and obj != ModelResource:
                try:  
                    print obj.Meta.keyhole
                    print name
                    print "here"
                    Resources.objects.get_or_create(name=name)
                except AttributeError as e:
                    pass
        print Resources.objects.count()

    
