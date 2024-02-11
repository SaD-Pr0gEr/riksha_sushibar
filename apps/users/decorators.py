from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View


def anonym_required_obj(func):
    def wrapper(self: View, request: HttpRequest, *args, **kwargs):
        if all([
            request.user, request.user.is_active,
            not request.user.is_anonymous, request.user.is_authenticated
        ]):
            # TODO: Django Messages
            # TODO: redirect исправить
            return redirect('/')
        return func(self, request, *args, **kwargs)
    return wrapper
