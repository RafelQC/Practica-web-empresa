from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = RichTextField(verbose_name='Contenido')
    img = models.ImageField(verbose_name='Imagen', upload_to='services')
    #datetime = camp de data i hora (auto_now_add=True, aquest cap s'auto emplenará amb l'hora real que se crei)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado día')
    #(auto_now_add=True, aquest cap s'auto emplenará amb l'hora real quan s'actualitza el camp)
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado día')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        #configuracion del orden en que deben estar los proyectos
        #en este caso ordenado por creación, de más reciente a más antiguo
        #por defecto lo organiza de mayor a menor (de más antiguo a nuevo)
        #por tanto si queremos que lo haga al revés ponemos signo negativo (-) delante
        ordering = ["-created"]
    
    #siempre nos devolvera el nombre que le hayamos especificado en title
    def __str__(self):
        return self.title