from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.forms import UserChangeForm, UserCreationForm
from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'phone_number', 'is_active', 'is_superuser']
    list_filter = ['is_superuser']
    readonly_fields = ['password', 'date_joined', 'last_login']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal info', {'fields': [
            'first_name', 'last_name', 'phone_number',
        ]}),
        ('Activity', {'fields': ['date_joined', 'last_login']}),
        ('Account permissions', {'fields': ['is_active', 'is_superuser']}),
    ]
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': [
                    'email', 'password1', 'password2',
                    'first_name', 'phone_number', 'is_active', 'is_superuser'
                ],
            },
        ),
    ]
    search_fields = ['email']
    filter_horizontal = []
    ordering = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
