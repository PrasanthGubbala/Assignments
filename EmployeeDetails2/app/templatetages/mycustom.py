from django import template

register = template.Library()
users = 0
@register.simple_tag()
def totalUsers(users):
    users =+users
    return users
