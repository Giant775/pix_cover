from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Safely retrieves an item from a dictionary using a key."""
    return dictionary.get(key, None)
