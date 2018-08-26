from django import template

register = template.Library()


@register.filter(name='solve_attachment_type')
def solve_attachment_type(value):
    return_value = '<img src=%s>' % value['url'] if value['type'] == 'image' else value['name']
    return return_value
