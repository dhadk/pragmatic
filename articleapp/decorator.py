from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(function):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return function(request, *args, **kwargs)
    return decorated
