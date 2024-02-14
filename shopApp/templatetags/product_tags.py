from django import template
from shopApp.models import Category

register = template.Library()

@register.filter
def category_filter(qs, cid):
    return qs.filter(category_id=cid)

@register.filter
def get_chiled_cats(obj):
    return Category.objects.filter(parent = obj)