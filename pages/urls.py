from django.urls import path
#hem d'importar les (core.views), per tant posam "from ." perque ja esteim a core i importam views
from . import views

urlpatterns = [
    #le pasamos a la URL el numero de la primary key para que cargue el contenido deseado
    #el valor que le pasa es una cadena de caracteres y por eso lo tenemos que pasar a integer, porque queremos un numero, no una cadena
    path('<int:page_id>/', views.page, name="page")
]