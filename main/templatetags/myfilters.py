
from django import template

register = template.Library()

def left(text, n):
    return text[:n]

@register.filter
def abstract(value):
    length = 240
    if not value or len(value) <= length:
        return value
    return f'{left(value, length)}...'