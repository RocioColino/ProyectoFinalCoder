from django.contrib import admin
from django.urls import path, include
from . import views
from Blog.views import BlogView, PostDetailView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView, AddCommentView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    #path('blog/', views.blog, name="blog"),
    #path('lugares/', views.lugares, name="lugares"),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post_detalles/<int:pk>', PostDetailView.as_view(), name='post-detalles'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post_detalles/update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post_detalles/<int:pk>/delete_post/', DeletePostView.as_view(), name='delete_post'),
    path('post_detalles/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('busqueda_post/', views.busqueda_post, name='busqueda_post'),
    ]
