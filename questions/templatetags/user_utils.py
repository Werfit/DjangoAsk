from django import template

register = template.Library()


@register.filter
def count(queryset):
    return queryset.count()
