from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.users.managers import CustomUserManager
from apps.users.validators import check_phone_number_uz


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, null=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(_('Superuser status'))
    phone_number = models.BigIntegerField(
        _('Phone number'),
        unique=True,
        validators=(check_phone_number_uz,)
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'phone_number']
    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
