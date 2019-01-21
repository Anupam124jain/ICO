from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.models import User


def user_is_valid(function):
    def wrap(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        try:
            if User.objects.get(pk=user_id):
                return function(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    return wrap
