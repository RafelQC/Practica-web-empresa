from django.contrib import admin

from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    
    #readonly_fields = ('created', 'updated',)
    
    #el camp KEY i NAME de SOCIAL l'hem d'amagar dels que no siguin desarrolladors per a que no modifiquin aquells camps
    #ja que si els poden tocar poden fer que falli el footer de l'HTML
    def get_readonly_fields(self, request, obj=None):
        #miram si l'usuari que esta executant aquest model a l'admin és un usuari de Personal i per tant no es el superusuari
        if request.user.groups.filter(name="Personal").exists():
            #els camps KEY i NAME quedaran només com a LECTURA
            return('key', 'name')
        else:
            #si no pertany a Personal es mostrará com per a un superUSER
            return('created', 'updated')
admin.site.register(Link, LinkAdmin)