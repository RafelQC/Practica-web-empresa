from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    #en la parte de creacion del Post, para que nos aparezca el campo autorellenado
    readonly_fields = ('created', 'updated')
    #en la parte de visualización de todos los post para que nos aparezca no solo el titulo si no los siguientes datos
    list_display = ('title', 'author', 'published', 'post_categories')
    #me ordena en la parte de visualización de todos los post por autor y despues por orden de publicación
    ordering = ('author', 'published')
    #sistema de busqueda en el pandel administrador por titulo y contenido, autor
    #si ponemos por autor (que es una clave foranea) nos dara error, hay que poner "__username", pasa igual con category al ser clave manytomany
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    #filtración por fechas de publicación (esto con muchas publicacions se ve mejor en el panel admin)
    date_hierarchy = 'published'
    #filtro que se ve a la derecha por autor y categorias
    list_filter = ('author__username', 'categories__name')

    #las categorias al ser una relación many to meny tenemos que pasarlo a algo legible
    #estudiar porque no lo pillo como lo hace
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    #cambiamos el nombre a una función para que se vea mejor en el pandel admin
    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)