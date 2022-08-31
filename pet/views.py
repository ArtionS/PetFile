from django.shortcuts import render, redirect

# Paquete para pedir que se este en modo login y pedir permisos
from django.contrib.auth.decorators import login_required , permission_required
# @login_required
# @permission_required('pet.view_pet', raise_exception=True)

# Forms
from .forms import PetForm
from pet_type.models import PetType

# Create your views here.


@login_required
@permission_required('pet.view_pet', raise_exception=True)
def PetList(request):
    context = {
        'pets': request.user.pet_set.all()
    }
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['pets'] = context['pets'].filter(name__icontains=search_input)
        # context['pets'] = context['pets'].filter(name__startswith=search_input)
    context['search_input'] = search_input
    return render(request, "pet/pet_list.html", context)


@login_required
@permission_required('pet.view_pet', raise_exception=True)
def PetDetail(request, pk):
    return render(request, "pet/pet_detail.html", {'pet': request.user.pet_set.get(id=pk)})


@login_required
@permission_required('pet.add_pet', raise_exception=True)
def PetCreate(request):
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


@login_required
@permission_required('pet.change_pet', raise_exception=True)
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


@login_required
@permission_required('pet.delete_pet', raise_exception=True)
def PetDelete(request, pk):
    if request.method == 'POST':
        mypet = request.user.pet_set.get(id=pk)
        mypet.delete()
        return redirect('pet_list')
    # if a GET (or any other method) we'll create a blank form
    else:
        mypet = request.user.pet_set.get(id=pk)
        form = PetForm()
    return render(request, 'pet/pet_confirm_delete.html', {'form': form, 'pet': mypet})
