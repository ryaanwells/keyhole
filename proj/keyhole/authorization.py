from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

from django.conf import settings
from django.core.exceptions import FieldError

class KeyholeAuthorization(Authorization):

    def __init__(self):
        self.usr = "user"

        if hasattr(settings, 'KEYHOLE_USER_FIELD'):
            self.usr = settings.KEYHOLE_USER_FIELD

    def base_checks(self, request):
        return hasattr(request, 'user')

    def read_list(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        query = {self.usr: bundle.request.user}
        
        try:
            object_list = object_list.filter(**query)
        except FieldError:
            raise Unauthorized("Cannot confirm user table.")
            
        return object_list
        
    def read_detail(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        if getattr(bundle.obj, self.usr, None) is None:
            raise Unauthorized("Cannot confirm key user.")

        if getattr(bundle.obj, self.usr) != bundle.request.user:
            raise Unauthorized("You do not own that key.")
        
        return True

    def create_list(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        return object_list

    def create_detail(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        if getattr(bundle.obj, self.usr, None) is None:
            raise Unauthorized("Cannot confirm key user.")

        if getattr(bundle.obj, self.usr) != bundle.request.user:
            raise Unauthorized("You do not own that key.")
        
        return True

    def update_list(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        allowed = []

        for obj in object_list:
            if getattr(obj, self.usr, None) is None:
                continue
            if getattr(obj, self.usr) == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        if getattr(bundle.obj, self.usr, None) is None:
            raise Unauthorized("Cannot confirm key user.")

        if getattr(bundle.obj, self.usr) != bundle.request.user:
            raise Unauthorized("You do not own that key.")
        
        return True

    def delete_list(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        query = {self.usr: bundle.request.user}
        
        try:
            object_list = object_list.filter(**query)
        except FieldError:
            raise Unauthorized("Cannot confirm user table.")

        return object_list

    def delete_detail(self, object_list, bundle):
        if not self.base_checks(bundle.request):
            raise Unauthorized("Cannot confirm request user")

        if getattr(bundle.obj, self.usr, None) is None:
            raise Unauthorized("Cannot confirm key user.")

        if getattr(bundle.obj, self.usr) != bundle.request.user:
            raise Unauthorized("You do not own that key.")
        
        return True

