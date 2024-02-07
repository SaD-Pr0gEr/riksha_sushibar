from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, BaseUserCreationForm

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
