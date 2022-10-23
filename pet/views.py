from django.shortcuts import render, redirect
from django.contrib import messages

"""
Decoradores para validar que se tengan los permisos y que se este logueado
"""
from django.contrib.auth.decorators import login_required, permission_required

# @login_required # Decorador para estar Logeado
# @permission_required('pet.view_pet', raise_exception=True)  # Cecorador para los permisos

"""
Formulario de la mascota para las funciones de Create and Update
"""
from .forms import PetForm

"""
Lista de tipos de animaless para los fprmularios de Create and Update
"""
from pet_type.models import PetType

"""
Modelo de coneccion para asignacion de deño a la mascota
"""
from veterinary.models import ConectionUV

"""
Bloque Funciones para las mascotas
"""


# Funcion que saca los datos necesarios para mostrar la lista de mascotas
@login_required
@permission_required('pet.view_pet', raise_exception=True)
def PetList(request):
    if request.user.groups.filter(name='group_user').exists():
        pets = request.user.pet_set.all()

    # variable que puede afectar la busqueda de mascotas
    search_input = request.GET.get('search-area') or ''

    context = {
        'pets': pets
    }

    # Filtrado de las mascotas con respecto al serah_input
    if search_input:
        context['pets'] = context['pets'].filter(name__icontains=search_input)
        # context['pets'] = context['pets'].filter(name__startswith=search_input)
    context['search_input'] = search_input
    return render(request, "pet/pet_list.html", context)


# funcion que muestra los detalles de una mascota
@login_required
@permission_required('pet.view_pet', raise_exception=True)
def PetDetail(request, id_pet):
    return render(request, "pet/pet_detail.html", {'pet': request.user.pet_set.get(id=id_pet)})


# funcion para rear una mascota ya sea POST or GET
@login_required
@permission_required('pet.add_pet', raise_exception=True)
def PetCreate(request, id_user):
    """
    Metodo POST Para dar de alta a una mascota
    """
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            """
            Validar si es usuario o veterinario
            """
            # for Vet
            if request.user.groups.filter(name='group_vet').exists():
                con = ConectionUV.objects.filter(user_id=request.user)
                user = con[0].vets.get(id=id_user)
                form.instance.owner = user
            # for User
            if request.user.groups.filter(name='group_user').exists():
                form.instance.owner = request.user

            form.save()

            if request.user.groups.filter(name='group_vet').exists():
                return redirect('user_pet_detail', id_user, form.instance.id)

            if request.user.groups.filter(name='group_user').exists():
                return redirect('pet_detail', form.instance.id)
        else:
            print(form.errors)
            message = form.errors
            messages.error(request, message)

    # if a GET (or any other method) we'll create a blank form

    context = {
        'form': PetForm(),
        'pet_type_list': PetType.objects.all(),
    }
    return render(request, 'pet/pet_form.html', context)


# funion que nos permite hacer un update a un masota
@login_required
@permission_required('pet.change_pet', raise_exception=True)
def PetUpdate(request, id_user, id_pet):
    mypet = {}
    # en el post asignamos los nuevos valores a las mascota si es que existen
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            """
            Validar si es usuario o veterinario
            """
            if request.user.groups.filter(name='group_vet').exists():
                con = ConectionUV.objects.filter(user_id=request.user)
                user = con[0].vets.get(id=id_user)
                mypet = user.pet_set.get(id=id_pet)

            if request.user.groups.filter(name='group_user').exists():
                mypet = request.user.pet_set.get(id=id_pet)

            mypet.name = form['name'].value()
            mypet.type_animal = form['type_animal'].value()
            mypet.raze = form['raze'].value()
            mypet.gender = form['gender'].value()
            mypet.description = form['description'].value()
            mypet.birth_day = form['birth_day'].value()

            if form['picture'].value():
                mypet.picture = form['picture'].value()

            mypet.save()

            if request.user.groups.filter(name='group_vet').exists():
                return redirect('user_pet_detail', id_user, id_pet)

            if request.user.groups.filter(name='group_user').exists():
                return redirect('pet_detail', id_pet)

        else:
            # print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:

        if request.user.groups.filter(name='group_vet').exists():
            con = ConectionUV.objects.filter(user_id=request.user)
            user = con[0].vets.get(id=id_user)

            mypet = user.pet_set.get(id=id_pet)

        if request.user.groups.filter(name='group_user').exists():
            mypet = request.user.pet_set.get(id=id_pet)

        mypet.birth_day = mypet.birth_day.strftime("%Y-%m-%d")

    context = {
        'pet_type_list': PetType.objects.all(),
        'form': PetForm(),
        'pet': mypet,
    }

    return render(request, 'pet/pet_form.html', context)


# funcino para borrar una mascota
@login_required
@permission_required('pet.delete_pet', raise_exception=True)
def PetDelete(request, id_pet):
    mypet = request.user.pet_set.get(id=id_pet)
    # Si se asepta el eliminar a la mascota se ejecuta el POST
    if request.method == 'POST':
        mypet.delete()
        return redirect('pet_list')
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'pet/pet_confirm_delete.html', {'pet': mypet})
