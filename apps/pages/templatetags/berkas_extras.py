from django import template

register = template.Library()

@register.filter
def urutan_for(berkas, jenis_hak):
    return berkas.get_urutan(jenis_hak)
