from django.conf import settings
import os, sys, inspect
from itertools import chain
from importlib import import_module
from tastypie.resources import ModelResource
from models import Resources

if hasattr(settings, "KEYHOLE"):
    for res in settings.KEYHOLE["resources"]:
        imports = import_module(res)
        for name, obj in inspect.getmembers(imports):
            if inspect.isclass(obj) and issubclass(obj, ModelResource) and obj != ModelResource:
                print name
                try:  
                    print obj.Meta.keyhole
                    print "here"
                    Resources.objects.get_or_create(name=name)
                except Exception as e:
                    print e
                    pass
        print Resources.objects.count()


if hasattr(settings, "KEYHOLEs"):
    print os.getcwd()
    objects = []
    for model in settings.KEYHOLE["models"]:
        imports = __import__(model, fromlist=settings.KEYHOLE["models"][model])
        for imp in settings.KEYHOLE["models"][model]:
            print imp
            print getattr(imports, imp)
            objects.append(getattr(imports, imp))
        
    print len(objects)
    print objects[0].__name__
    # for imp in imports:
    #     print imp
    #     for name, obj in inspect.getmembers(imp):
    #         if inspect.isclass(obj):
    #             print obj
    
