from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views import View

from .decorators import anonym_required_obj, login_required_obj
from .forms import LoginForm, UserCreationForm
from ..products.models import Category


class UserLogin(View):
    template = 'users/pages/auth_page.html'

    @anonym_required_obj
    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(
            request,
            self.template,
            {
                'title': _('Signin'),
                'login': True,
                'form': form,
                'product_categories': Category.objects.all(),
            }
        )

    @anonym_required_obj
    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        auth_error = False
        if not form.is_valid():
            auth_error = True
        auth_user = authenticate(**form.cleaned_data)
        if not auth_user:
            form.add_error(
                'email',
                _('User with that email and password not found')
            )
            auth_error = True
        if auth_error:
            return render(
                request,
                self.template,
                {
                    'title': _('Signin'),
                    'login': True,
                    'form': form
                }
            )
        login(request, auth_user)
        return redirect('products:home')


class UserRegister(View):
    template = 'users/pages/auth_page.html'

    @anonym_required_obj
    def get(self, request: HttpRequest) -> HttpResponse:
        form = UserCreationForm()
        return render(
            request,
            self.template,
            {
                'title': _('Signup'),
                'form': form,
                'product_categories': Category.objects.all()
            }
        )

    @anonym_required_obj
    def post(self, request: HttpRequest) -> HttpResponse:
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                self.template,
                {
                    'title': _('Signup'),
                    'form': form
                }
            )
        form.save()
        # TODO: Django Messages
        return redirect('users:users_login')


class UsersLogoutView(View):

    @login_required_obj
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('users:users_login')
