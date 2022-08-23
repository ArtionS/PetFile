from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# Paquete para pedir que se este en modo login
from django.contrib.auth.mixins import LoginRequiredMixin

# Modelo de mascota
from .models import Pet

# Forms
from .forms import PetForm


# import cgi


# Create your views here.


def PetList(request):
    return render(request, "pet/pet_list.html", {'pets': request.user.pet_set.all()})


def PetDetail(request, pk):
    return render(request, "pet/pet_detail.html", {'pet': request.user.pet_set.get(id=pk)})


def PetCreate(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return PetList(request)
        else:
            print('/ No thanks/')
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', {'form': form})


def PetUpdate(request, pk):
    print("Update Pet")
    if request.method == 'POST':
        print("Update Pet POST")
        form = PetForm(request.POST)
        if form.is_valid():
            # form.save()
            return PetList(request)
        else:
            print('/ No thanks/')
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:

        print("Update Pet GET")
        mypet = request.user.pet_set.get(id=pk)
        form = PetForm()

        # form.instance.owner = mypet.owner
        # form.instance.name = mypet.name
        # form.instance.type_animal = mypet.type_animal
        # form.instance.raze = mypet.raze
        # form.instance.gender = mypet.gender
        # form.instance.description = mypet.description
        # form.birth_day. = mypet.birth_day
        # form.instance.picture = mypet.picture

        print(form)
        mypet.birth_day = mypet.birth_day.strftime("%Y-%m-%d")
        print(mypet.birth_day)

    return render(request, 'pet/pet_form.html', {'form': form , 'pet' : mypet})


# class PetUpdate(LoginRequiredMixin, UpdateView):
#     model = Pet
#     # fields = '__all__'
#     fields = [
#         'name',
#         'type_animal',
#         'raze',
#         'gender',
#         'description',
#         'birth_day',
#         'picture',
#     ]
#     success_url = reverse_lazy('pet_list')


class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet/pet_confirm_delete.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('pet_list')
