from django.urls import path
#hem d'importar les (core.views), per tant posam "from ." perque ja esteim a core i importam views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact')
] 