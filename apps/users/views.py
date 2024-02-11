from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views import View

from apps.users.forms import LoginForm


class UserLogin(View):
    template = 'users/pages/auth_page.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(
            request,
            self.template,
            {
                'title': _('Signin'),
                'login': True,
                'form': form
            }
        )

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
        # TODO: Когда добавишь гл. страницу поменяй редирект
        return redirect('/')
