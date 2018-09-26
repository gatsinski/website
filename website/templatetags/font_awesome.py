from django import template

from website.contrib.contacts.constants import ICON_MAP

register = template.Library()


@register.filter
def icon(value):
    return ICON_MAP[value]
