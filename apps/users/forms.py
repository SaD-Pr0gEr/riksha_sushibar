from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField, BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class UserCreationForm(BaseUserCreationForm):
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'placeholder': _('Password'), 
            'class': 'form-field'
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'placeholder': _('Password repeat'), 
            'class': 'form-field'
        }),
        strip=False,
        help_text=_('Enter the same password as before, for verification.'),
    )

    def save(self, commit=True):
        user = super().save(False)
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'email': forms.EmailInput(
                {'placeholder': _('email'), 'class': 'form-field'}
            ),
            'first_name': forms.TextInput(
                {'placeholder': _('First name'), 'class': 'form-field'}
            ),
            'last_name': forms.TextInput(
                {'placeholder': _('Last name'), 'class': 'form-field'}
            ),
            'phone_number': forms.NumberInput(
                {'placeholder': _('Phone number'), 'class': 'form-field'}
            )
        }


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
