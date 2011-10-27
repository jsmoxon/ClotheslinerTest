from django import template

register = template.Library()

@register.filter(name='select')
def select(d, key):
    return d[key]

@register.filter(name='get_range')
def get_range(v1,v2):
	return range(v1,v2)
