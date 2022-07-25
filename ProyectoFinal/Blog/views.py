from ssl import CertificateError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Blog.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from .models import *
from django.urls import reverse_lazy
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
    #ordering=['-id']
    ordering=['-fecha']

class PostDetailView(DetailView):
    model=Post
    template_name='Blog/post_detalles.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name= 'Blog/add_post.html'
    #fields='__all__'

class AddCategoryView(CreateView):
    model=Categoria
    #form_class=PostForm
    template_name= 'Blog/add_category.html'
    fields='__all__'
    
class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='Blog/update_post.html'
    #fields='__all__'

class DeletePostView(DeleteView):
    model=Post
    template_name='Blog/delete_post.html'
    success_url= reverse_lazy('blog')

def lugares(request):
    return render(request, 'Blog/lugares.html', {})
