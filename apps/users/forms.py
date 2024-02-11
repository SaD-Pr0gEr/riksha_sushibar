from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number']


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        {'placeholder': _('email'), 'class': 'form-field'}
    ))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(
        {'placeholder': _('Password'), 'class': 'form-field'}
    ))
