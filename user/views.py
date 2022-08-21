# from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import reverse_lazy

# Vista para el login
from django.contrib.auth.views import LoginView
# aquetes para la creacion de la pagina registro
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')


class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage , self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')
        return super(RegisterPage, self).get(*args, **kwargs)
