from django.shortcuts import redirect

# Vista para el login and register
# from .views import LoginView
# aquetes para la creacion de la pagina registro
from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# ------------------------------------------------------------- to Login
import warnings
from urllib.parse import urlparse, urlunparse

from django.conf import settings

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import login as auth_login
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView


# Create your views here.

from .forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import Group

from django.contrib.auth.views import RedirectURLMixin


# vista para deplegar la pagina de login
class LoginView(RedirectURLMixin, FormView):
    """
    Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                self.redirect_field_name: self.get_redirect_url(),
                "site": current_site,
                "site_name": current_site.name,
                **(self.extra_context or {}),
            }
        )
        return context


# Vista para desplegar el login
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')


# vista para deplegas la pagina de registro
class RegisterPage(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):


        user = form.save()
        if user is not None:
            login(self.request, user)
            if form["group"].value() :
                my_group = Group.objects.get(name='group_vet')
                my_group.user_set.add(user)
            else:
                my_group = Group.objects.get(name='group_user')
                my_group.user_set.add(user)
        return super(RegisterPage , self).form_valid(form)



    def get(self, *args, **kwargs):
        print("IN REGISTER PAGE : GET")
        if self.request.user.is_authenticated:
            return redirect('home_page')
        return super(RegisterPage, self).get(*args, **kwargs)
