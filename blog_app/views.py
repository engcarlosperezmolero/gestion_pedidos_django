from django.shortcuts import render

from .models import Post, Categoria
# Create your views here.


def blog(request):
    categorias_unicas = Categoria.objects.all()
    posts = Post.objects.all()  # importando absolutamente todo lo creado en la Clase Post de models
    # categorias = Post.categorias.all()
    return render(request, 'blog_app/blog.html',
                  {"posts": posts,
                   "categorias": [[j.nombre for j in i] for i in [post.categorias.all() for post in posts]],
                   "categorias_unicas": categorias_unicas,

                   })


def categoria(request, categoria_id):
    categorias_unicas = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)

    return render(request, "blog_app/categoria.html",
                  {"categoria": categoria,
                   "categorias": [[j.nombre for j in i] for i in [post.categorias.all() for post in posts]],
                   "posts": posts,
                   "categorias_unicas": categorias_unicas,
                   })
