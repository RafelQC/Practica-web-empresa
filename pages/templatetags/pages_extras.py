from django import template
from pages.models import Page

#en aquest apartat podem crear els nostres templatetag

#cream variable amb nom register on fa referencia a la libreria template.Library(), un metode
register = template.Library()
#transformarm una funció "get_pages_list" en un simple tag
@register.simple_tag

#aquí definim quins valors volem retornar al template tag
#en aquest cas volem agafar de la base de dades Page tots els seus valors y retornarlos
def get_pages_list():
    pages = Page.objects.all()
    return pages