from django.shortcuts import render

from .models import Post, Categoria
# Create your views here.


def blog(request):
    posts = Post.objects.all()  # importando absolutamente todo lo creado en la Clase Post de models
    # categorias = Post.categorias.all()
    return render(request, 'blog_app/blog.html', {"posts": posts,
                                                  "categorias": [[j.nombre for j in i] for i in [post.categorias.all() for post in posts]]

                                                  })


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog_app/categoria.html", {"categoria": categoria, "posts": posts, "categorias": [[j.nombre for j in i] for i in [post.categorias.all() for post in posts]]})
