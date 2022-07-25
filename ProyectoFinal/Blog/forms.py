from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('titulo', 'subtitulo','autor', 'cuerpo')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.Select(attrs={'class':'form-control'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('titulo', 'subtitulo', 'cuerpo')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control'}),
        }