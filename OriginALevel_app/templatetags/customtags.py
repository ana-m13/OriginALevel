from django import template
from django.db.models import Avg, Count, Sum

# to creat html tags in django, I need to create some functions 
# functions help perform functions in django that otherwise would need subroutines for
    
register = template.Library()

@register.filter
def rangeint(int):
    result = [i for i in range(int)]
    return result

@register.filter
def times(int):
    return range(int)