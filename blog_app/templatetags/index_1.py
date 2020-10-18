from django.template.library import Library
register = Library()


@register.filter(is_safe=True)
def index(indexable, i):
    return indexable[i]
