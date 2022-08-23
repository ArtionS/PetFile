from django.shortcuts import render

from django.urls import reverse_lazy, reverse

# Paquete para pedir que se este en modo login
from django.contrib.auth.mixins import LoginRequiredMixin

# Modelo de mascota
from .models import Pet

# Forms
from .forms import PetForm

# Create your views here.


def PetList(request):
    return render(request, "pet/pet_list.html", {'pets': request.user.pet_set.all()})


def PetDetail(request, pk):
    return render(request, "pet/pet_detail.html", {'pet': request.user.pet_set.get(id=pk)})


def PetCreate(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return PetList(request)
        else:
            # print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PetForm()
    return render(request, 'pet/pet_form.html', {'form': form})


def PetUpdate(request, pk):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            mypet = request.user.pet_set.get(id=pk)

            mypet.name = form['name'].value()
            mypet.type_animal = form['type_animal'].value()
            mypet.raze = form['raze'].value()
            mypet.gender = form['gender'].value()
            mypet.description = form['description'].value()
            mypet.birth_day = form['birth_day'].value()
            mypet.picture = form['picture'].value()

            mypet.save()
            return PetList(request)
        else:
            print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        mypet = request.user.pet_set.get(id=pk)
        mypet.birth_day = mypet.birth_day.strftime("%Y-%m-%d")
        form = PetForm()
    return render(request, 'pet/pet_form.html', {'form': form, 'pet': mypet})


def PetDelete(request, pk):
    print("Delete Pet")
    if request.method == 'POST':
        print("Delete Pet POST")
        mypet = request.user.pet_set.get(id=pk)
        print(mypet)
        print(mypet.__dict__)
        mypet.delete()
        return PetList(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        print("Delete Pet GET")
        mypet = request.user.pet_set.get(id=pk)
        form = PetForm()
    return render(request, 'pet/pet_confirm_delete.html', {'form': form, 'pet': mypet})

# class PetDelete(LoginRequiredMixin, DeleteView):
#     model = Pet
#     template_name = 'pet/pet_confirm_delete.html'
#     context_object_name = 'pet'
#     success_url = reverse_lazy('pet_list')
