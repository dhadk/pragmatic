from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(function):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return function(request, *args, **kwargs)
    return decorated
