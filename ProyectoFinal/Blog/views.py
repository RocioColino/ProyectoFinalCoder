from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def inicio(request):
    return render(request, 'Blog/inicio.html', {} )

def about(request):
    return render(request, 'Blog/about.html', {})

#def blog(request):
    return render(request, 'Blog/blog.html', {})

class BlogView(ListView):
    model=Post
    template_name='Blog/blog.html'

class PostDetailView(DetailView):
    model=Post
    template_name='Blog/post_detalles.html'


def lugares(request):
    return render(request, 'Blog/lugares.html', {})
