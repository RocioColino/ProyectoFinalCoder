from dataclasses import fields
from django import forms
from .models import *

class NuevoBlog(forms.ModelForm):
    class Meta: 
        model=Post
        fields='__all__'