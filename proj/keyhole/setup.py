from models import Resources, Methods, Key
from resources import ResourcesResource, MethodsResource, KeyResource
from tastypie.api import Api


from django.core.exceptions import ImproperlyConfigured

class Keyhole(object):
    
    def __init__(self):
        self._resources = {}

    def register(self, api):
        resources = getattr(api, '_registry', None)
        if resources is None:
            raise ImproperlyConfigured("API %r does not have any Resources." % api.api_name)

        for name in resources:
            if getattr(resources[name], '_meta', None) is not None:
                attrs = getattr(resources[name]._meta, 'keyhole', None)
                if attrs is not None:
                    for m in range(len(attrs)):
                        attrs[m] = attrs[m].upper()
                        
                    methods = Methods.objects.filter(name__in=attrs)
                    
                    res = Resources.objects.get_or_create(name=name)[0]
                    
                    for m in methods:
                        res.allowed_methods.add(m)
                        
                    res.save()

    @property
    def urls(self):
        api = Api('keyhole')
        api.register(ResourcesResource())
        api.register(MethodsResource())
        api.register(KeyResource())
        return api.urls

        
