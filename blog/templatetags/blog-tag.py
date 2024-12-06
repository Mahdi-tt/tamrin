from django import template

register = template.Library()
@register.filter(name='short')
def function(value,arg=20):
    return value[:arg]+'...'