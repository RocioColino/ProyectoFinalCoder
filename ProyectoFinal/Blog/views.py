from ssl import CertificateError
from django.shortcuts import render, redirect
from Blog.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm

from .models import *
#from .forms import *

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

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name= 'Blog/add_post.html'
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name='Blog/update_post.html'
    fields='__all__'

def lugares(request):
    return render(request, 'Blog/lugares.html', {})
