from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(function):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        print(type(profile), type(profile.user))
        if not profile.user == request.user:
            print('잘못됨')
            return HttpResponseForbidden()
        print('완료')
        return function(request, *args, **kwargs)
    return decorated
