from django import template

register = template.Library()


@register.filter
def is_image(value):
    return value.startswith('image/')
