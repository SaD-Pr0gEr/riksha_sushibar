from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile
from django.utils.translation import gettext_lazy as _


def validate_icon(value: FieldFile) -> bool:
    for format_ in settings.ICON_FORMATS:
        if value.name.endswith(format_):
            return True
    else:
        raise ValidationError(_(
            f'Icon file "{value}" should be with formats '
            + ', '.join(settings.ICON_FORMATS)
        ))
