from ssl import CertificateError
from django.shortcuts import render, redirect
from Blog.models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView


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

#class PostCrear(CreateView):
  #  model=Post
   # success_url: "/Blog/post/list"
def nuevoblog(request):
    if request.method=="POST":
        form=NuevoBlog(request.POST)
        if form.is_valid:
            form.save()
            return redirect('blog')
    else:
        form=NuevoBlog()
        return render(request, 'Blog/nuevoblog.html', {"form":form})

def lugares(request):
    return render(request, 'Blog/lugares.html', {})
