#from django.contrib import admin
from django.urls import path
from .views import UserEditView, UserRegisterView, ShowProfileView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('perfil/<int:pk>', ShowProfileView.as_view(), name='show_profile_page'),
]
