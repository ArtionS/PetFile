"""
Filtro para template | Filtro para validad pertenencia a un grupo
"""
from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

