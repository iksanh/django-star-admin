# app/templatetags/split_points.py
from django import template
import re

register = template.Library()

@register.filter
def split_points(value):
    if not value:
        return []
    parts = re.split(r'\d+\.\s*', value)
    return [p.strip() for p in parts if p.strip()]
