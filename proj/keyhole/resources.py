from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

from django.contrib.auth.models import User

from models import Resources, Methods, Key

class UserResource(ModelResource):
    class Meta():
        queryset = User.objects.all()
        resource_name = 'user'
        always_return_data = True
        include_resource_uri = True

class MethodsResource(ModelResource):
    class Meta():
        queryset = Methods.objects.all()
        
        resource_name = 'methods'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True    

class ResourcesResource(ModelResource):
    allowed_methods = fields.ToManyField(MethodsResource, 'allowed_methods')
    class Meta():
        queryset = Resources.objects.all()
        resource_name = 'resources'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True

class KeyResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    locks = fields.ForeignKey(ResourcesResource, 'locks', null=True)
    allowed_methods = fields.ToManyField(MethodsResource, 'allowed_methods', full=True)

    class Meta():
        queryset = Key.objects.all()
        resource_name = 'key'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True

    def dehydrate(self, bundle):
        methods = []
        # print bundle.data['user']
        for method in bundle.data['allowed_methods']:
            methods.append(method.data['name'])
        bundle.data['allowed_methods'] = methods
        return bundle

    def obj_create(self, bundle, **kwargs):
        print bundle.request.user
        print kwargs
        return super(KeyResource, self).obj_create(bundle)
