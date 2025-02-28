from django import template                                                                                                                                                        
from django.template.defaultfilters import stringfilter
from pixcoverapp.database import Categories

register = template.Library()

@register.filter
@stringfilter
def space2Dash(s):
    return s.replace(' ', '_');

@register.filter(name='split')
def split(value, key):
  """
    Returns the value turned into a list.
  """
  return value.split(key)

@register.filter(name='getabname')
def getabname(value):
  """
    Returns the value turned into a list.
  """
  if (len(value.split()) > 1):
    return value.split()[0] + " " + value.split()[1][0] + "."
  return value

@register.filter(name='getcategoryname')
def getcategoryname(value):
  """
    Return the category name of the user
  """
  categories = Categories.objects.filter().values()
  for x in categories:
    if (x['id'] == value):
      return x['category']
    
  return 'Nothing'