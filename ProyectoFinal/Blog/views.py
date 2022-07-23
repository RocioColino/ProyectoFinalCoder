from django.shortcuts import render


def inicio(request):
    return render(request, 'Blog/inicio.html', {} )

def about(request):
    return render(request, 'Blog/about.html', {})

def blog(request):
    return render(request, 'Blog/blog.html', {})

def lugares(request):
    return render(request, 'Blog/lugares.html', {})
