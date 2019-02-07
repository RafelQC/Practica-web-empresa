from django.urls import path
#hem d'importar les (core.views), per tant posam "from ." perque ja esteim a core i importam views
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),

    #le pasamos a la URL el numero de la primary key para que cargue el contenido deseado
    #el valor que le pasa es una cadena de caracteres y por eso lo tenemos que pasar a integer, porque queremos un numero, no una cadena
    path('category/<int:category_id>/', views.category, name="category"),
]