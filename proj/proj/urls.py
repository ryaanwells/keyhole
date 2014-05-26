from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from keyhole.setup import Keyhole
from mock.resources import UserResource, PicturesResource, AudioResource, FeedResource

api = Api()
kh = Keyhole()
api.register(UserResource())
api.register(PicturesResource())
api.register(AudioResource())
api.register(FeedResource())

kh.register(api)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^', include(kh.urls)),
)

