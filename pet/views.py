from django.shortcuts import render, redirect

# Decoradores para solicitar los permisos y que este logueado
from django.contrib.auth.decorators import login_required , permission_required
# @login_required
# @permission_required('pet.view_pet', raise_exception=True)

# Se importa el formulario de la mascota
from .forms import PetForm
# Se importa lalista de los tipos de animales
from pet_type.models import PetType

# Create your views here.


# Funcion que saca los datos necesarios para mostrar la lista de mascotas
@login_required
@permission_required('pet.view_pet', raise_exception=True)
def PetList(request):

    # variable que puede afectar la busqyueda de mascotas
    search_input = request.GET.get('search-area') or ''

    # se hace la peticion de todas las mascotas del ususario logeado
    context = {
        'pets': request.user.pet_set.all(),
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
def PetDetail(request, pk):
    return render(request, "pet/pet_detail.html", {'pet': request.user.pet_set.get(id=pk)})


# funcion para rear una mascota ya sea POST or GET
@login_required
@permission_required('pet.add_pet', raise_exception=True)
def PetCreate(request):
    # Metodo POST Para dar de alta a una mascota
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('pet_detail', form.instance.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PetForm()
        pet_type_list = PetType.objects.all()
    return render(request, 'pet/pet_form.html', {'form': form , 'pet_type_list': pet_type_list})


# funion que nos permite hacer un update a un masota
@login_required
@permission_required('pet.change_pet', raise_exception=True)
def PetUpdate(request, pk):
    # en el post asignamos los nuevos valores a las mascota si es que existen
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

            if form['picture'].value():
                mypet.picture = form['picture'].value()

            mypet.save()
            return redirect('pet_detail', mypet.id)
        else:
            # print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        mypet = request.user.pet_set.get(id=pk)
        mypet.birth_day = mypet.birth_day.strftime("%Y-%m-%d")
        form = PetForm()
    return render(request, 'pet/pet_form.html', {'form': form, 'pet': mypet})


# funcino para borrar una mascota
@login_required
@permission_required('pet.delete_pet', raise_exception=True)
def PetDelete(request, pk):

    mypet = request.user.pet_set.get(id=pk)
    # Si se asepta el eliminar a la mascota se ejecuta el POST
    if request.method == 'POST':
        mypet.delete()
        return redirect('pet_list')
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'pet/pet_confirm_delete.html', {'pet': mypet})
