from django import template

from ..utils import fix_url_query_params

register = template.Library()


@register.simple_tag
def fix_url(url: str, **query_params) -> str:
    return fix_url_query_params(url, **query_params)
