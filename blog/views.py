from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {'posts':posts})

#con el category_id le pasamos la primary key a la vista
def category(request, category_id):
    #en este caso no ponemos un "object.all()" porque no queremos todos los datos
    #esta vista nos servirá para filtrar entre categorias
    #get_object_or_404 nos pillará los valors de la base de datos con el valor que le hemos pasado de id
    #si no encuentra el valor, en vez de crashear, nos mostrara un error de 404 not found
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request,"blog/category.html", {'posts': posts})