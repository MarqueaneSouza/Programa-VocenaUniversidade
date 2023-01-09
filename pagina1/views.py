#LÓGICA DE NEGÓCIO
from django.shortcuts import render
from . models import Post

def home(request): #Carregar a home com todos os posts catálogados no banco de dados.
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pagina1/home.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'pagina1/post_detail.html', context)