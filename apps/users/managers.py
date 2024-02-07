from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(
        self, email: str, password: str, first_name: str,
        phone_number: int, **extra_params
    ):
        if not email:
            raise ValueError(_('Email cannot be null'))
        norm_email = self.normalize_email(email)
        extra_params['is_superuser'] = False
        password_hash = make_password(password)
        model = self.model(
            email=norm_email, password=password_hash, first_name=first_name,
            phone_number=phone_number, **extra_params
        )
        model.save(using=self._db)
        return model

    def create_superuser(
        self, email: str, password: str, first_name: str,
        phone_number: int, **extra_params
    ):
        extra_params['is_active'] = True
        user = self.create_user(
            email, password, first_name, phone_number,
            **extra_params
        )
        user.is_superuser = True
        user.save()
        return user
