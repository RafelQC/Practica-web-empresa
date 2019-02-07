"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    #afegim totes les URL que tenim a CORE sense haver d'importar les views aquí
    path('', include('core.urls')),
    #afegim les URL de services
    path('services/', include('services.urls')),
    #afegim les URL de blog
    path('blog/', include('blog.urls')),
    #afegim les URL de pages
    path('page/', include('pages.urls')),
    #afegim les URL de contact
    path('contact/', include('contact.urls')),
    #Paths del admin
    path('admin/', admin.site.urls), 
]

#configuració per poder veure les imatges a les proves que feim sense aplicaciones de bases de dades que ens permetin veure les imatges
#complicat d'entendre inicialment aquest codi
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)