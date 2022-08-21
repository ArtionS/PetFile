# from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Paquete para pedir que se este en modo login
from django.contrib.auth.mixins import LoginRequiredMixin

# Modelo de mascota
from .models import Pet

# Create your views here.


class PetList(LoginRequiredMixin, ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet/pet_list.html'

    def get_context_data(self, **kwargs):
        # print(kwargs)
        context = super().get_context_data(**kwargs)
        # print(context)

        context['pets'] = context['pets'].filter(owner=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            # context['pets'] = context['pets'].filter(name__icontains=search_input)
            context['pets'] = context['pets'].filter(name__startswith=search_input)
        context['search_input'] = search_input

        return context


class PetDetail(LoginRequiredMixin, DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'pet/pet_detail.html'


class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    # fields = '__all__'
    fields = [
        'name',
        'type_animal',
        'raze',
        'gender',
        'description',
        'birth_day',
        'picture',
        ]

    template_name = 'pet/pet_form.html'
    success_url = reverse_lazy('pet_list')

    def form_valid(self, form):
        # print("Form Valid Pet Create")
        # print("Self")
        # print(self)
        # print(self.__dict__)
        # print("form")
        # print(form)
        # print("Head")
        # print(self.head.__dict__)

        form.instance.owner = self.request.user
        return super(PetCreate, self).form_valid(form)


    # context_object_name = 'pet'
    # template_name = 'base/pet_form.html'



class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    # fields = '__all__'
    fields = [
        'name',
        'type_animal',
        'raze',
        'gender',
        'description',
        'birth_day',
        'picture',
    ]
    success_url = reverse_lazy('pet_list')


class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet/pet_confirm_delete.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('pet_list')
