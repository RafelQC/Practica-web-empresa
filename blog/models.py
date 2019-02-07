from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado día')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado día')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ["-created"]
    
    #siempre nos devolvera el nombre que le hayamos especificado en title
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    content = RichTextField(verbose_name = 'Contenido')
    published = models.DateTimeField(verbose_name = 'Fecha de publicación', default = now())
    img = models.ImageField(verbose_name = 'Imagen', blank = True, null = True, upload_to = 'blog')
    #añadimos una clave foranea, pues esta esta ligada a la base de datos de los usuarios de la web
    #on_delete = models.CASCADE esta opción nos elimina todos Post de un usuario al ser BORRADO
    #on_delete = models.PROTECT esta opción nos guarda los posts (hay que tener en cuenta poner blank y null en true para esta opción pues no existirá autor)
    author = models.ForeignKey(User, verbose_name = 'Autor', on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = 'Categorías')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado día')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado día')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ["-created"]
    
    #siempre nos devolvera el nombre que le hayamos especificado en title
    def __str__(self):
        return self.title

