from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from django.contrib.auth.models import User
from models import Pictures, Audio, Feed

class UserResource(ModelResource):
    class Meta():
        keyhole = ['get']
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True
        
class PicturesResource(ModelResource):
    class Meta():
        queryset = Pictures.objects.all()
        resource_name = 'picture'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True

class AudioResource(ModelResource):
    class Meta():
        queryset = Audio.objects.all()
        resource_name = 'audio'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True

class FeedResource(ModelResource):
    class Meta():
        queryset = Feed.objects.all()
        resource_name = 'feed'
        authorization = Authorization()
        always_return_data = True
        include_resource_uri = True
