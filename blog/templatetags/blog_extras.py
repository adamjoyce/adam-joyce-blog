from django import template

register = template.Library()

@register.filter
def key_value(dict, key):
    return dict[key]
