from cProfile import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from Blog.models import Perfil, User
from .forms import RegistroForm, EditProfileForm

class ShowProfileView(DetailView):
    model=Perfil
    template_name='Miembros/registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user=Perfil.object.all()
        context=super(ShowProfileView, self).get_context_data(*args,**kwargs)

        page_user=get_object_or_404(Perfil, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
        #return redirect('profiles:profile-update', pk=pk)








class UserRegisterView(generic.CreateView):
    form_class=RegistroForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('inicio')

    def get_object(self):
        return self.request.user


