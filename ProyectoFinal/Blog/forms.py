from django import forms
from .models import Post, Categoria



choices= Categoria.objects.all().values_list('nombre', 'nombre')
#choices=[('turismo', 'turismo'),('cafeterias', 'cafeterias'),('tradicional', 'tradicional')]
choice_list=[]
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('titulo', 'subtitulo','autor', 'categoria', 'cuerpo', 'fragmento')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            #'autor':forms.Select(attrs={'class':'form-control'}),
            'categoria':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control'}),
            'fragmento':forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('titulo', 'subtitulo', 'cuerpo', 'fragmento')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control'}),
            'fragmento':forms.Textarea(attrs={'class':'form-control'}),
        }