
from django.urls import path
from . import views
from Blog.views import BlogView, PostDetailView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    #path('blog/', views.blog, name="blog"),
    path('lugares/', views.lugares, name="lugares"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('post_detalles/<int:pk>', PostDetailView.as_view(), name="post-detalles"),

]
