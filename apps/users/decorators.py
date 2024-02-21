from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View


def anonym_required_obj(func):
    def wrapper(self: View, request: HttpRequest, *args, **kwargs):
        if all([
            request.user, request.user.is_active,
            not request.user.is_anonymous
        ]):
            # TODO: Django Messages
            return redirect('products:home')
        return func(self, request, *args, **kwargs)
    return wrapper


def login_required_obj(func):
    def wrapper(self: View, request: HttpRequest, *args, **kwargs):
        if any([
            not request.user, not request.user.is_active,
            request.user.is_anonymous,
        ]):
            # TODO: Django Messages
            return redirect('users:users_login')
        return func(self, request, *args, **kwargs)
    return wrapper
