from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication

from django.contrib.auth.models import User

from models import Resources, Methods, Key
from authorization import KeyholeAuthorization

class MethodsResource(ModelResource):
    class Meta():
        queryset = Methods.objects.all()
        allowed_methods = ['GET']
        resource_name = 'methods'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True    

class ResourcesResource(ModelResource):
    allowed_methods = fields.ToManyField(MethodsResource, 'allowed_methods', full=True)
    class Meta():
        queryset = Resources.objects.all()
        allowed_methods = ['GET']
        resource_name = 'resources'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True

class KeyResource(ModelResource):
    locks = fields.ForeignKey(ResourcesResource, 'locks', null=True)
    allowed_methods = fields.ToManyField(MethodsResource, 'allowed_methods', full=True)

    class Meta():
        queryset = Key.objects.all()
        resource_name = 'key'
        authorization = KeyholeAuthorization()
        authentication = BasicAuthentication()
        always_return_data = True
        include_resource_uri = True
        fields = ['locks', 'allowed_methods']

    def dehydrate(self, bundle):
        methods = []
        # print bundle.data['user']
        for method in bundle.data['allowed_methods']:
            methods.append(method.data['name'])
        bundle.data['allowed_methods'] = methods
        return bundle

    def obj_create(self, bundle, **kwargs):
        user = bundle.request.user
        return super(KeyResource, self).obj_create(bundle, user=user)
