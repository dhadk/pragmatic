from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(function):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return function(request, *args, **kwargs)
    return decorated
