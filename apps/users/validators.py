from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_phone_number_uz(value: int):
    if len(str(value)) != 12:
        ValidationError(_(f'Phone number "{value}" can\'t be more than 12 chars'))
