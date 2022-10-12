from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required
# @login_required
# @permission_required('pet.view_pet', raise_exception=True)

"""
Import the Form Tp Create an Edit Vaccines
"""
from .forms import VaccineForm

"""
Import the model Conection to search the Vaccines from the the User list
"""
from veterinary.models import ConectionUV


@login_required
@permission_required('vaccine.view_vaccine', raise_exception=True)
def VaccineList(request, id_user, id_pet):
    # Vaccine List
    vaccines = {}
    """
    A validation for user and vet, to see how is making the search
    """
    if request.user.groups.filter(name='group_vet').exists():
        vaccines = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .vaccine_set.all()

    if request.user.groups.filter(name='group_user').exists():
        vaccines = request.user\
            .pet_set.get(id=id_pet)\
            .vaccine_set.all()

    context = {
        'vaccines': vaccines,
        'id_user': id_user,
        'id_pet': id_pet,
    }

    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['vaccines'] = context['vaccines'].filter(name__icontains=search_input)
        # context['processes'] = context['processes'].filter(title__startswith=search_input)
    context['search_input'] = search_input

    return render(request, "vaccine/vaccine_list.html", context)


@login_required
@permission_required('vaccine.view_vaccine', raise_exception=True)
def VaccineDetail(request, id_user, id_pet, id_vac):
    vaccine = {}
    """
    A validation for user and vet, to see how is making the search
    """
    if request.user.groups.filter(name='group_vet').exists():
        vaccine = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .vaccine_set.get(id=id_vac)

    if request.user.groups.filter(name='group_user').exists():
        vaccine = request.user\
            .pet_set.get(id=id_pet)\
            .vaccine_set.get(id=id_vac)

    context = {
        'vaccine': vaccine,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    return render(request, "vaccine/vaccine_detail.html", context)


@login_required
@permission_required('vaccine.add_vaccine', raise_exception=True)
def VaccineCreate(request, id_user, id_pet):
    context = {}
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid() and request.user.groups.filter(name='group_vet').exists():

            form.instance.pet_id = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)

            form.save()

            return redirect('vaccine_list', id_user, id_pet)
        else:
            print('/ No thanks/')
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'form': VaccineForm(),
            'id_user': id_user,
            'id_pet': id_pet,
        }
    return render(request, "vaccine/vaccine_form.html", context)


@login_required
@permission_required('vaccine.change_vaccine', raise_exception=True)
def VaccineUpdate(request, id_user, id_pet, id_vac):
    my_vaccine = {}
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid() and request.user.groups.filter(name='group_vet').exists():

            my_vaccine = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)\
                .vaccine_set.get(id=id_vac)

            my_vaccine.name = form['name'].value()
            my_vaccine.save()

            return redirect('vaccine_detail', id_user, id_pet, my_vaccine.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        my_vaccine = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .vaccine_set.get(id=id_vac)

    context = {
        'form': VaccineForm(),
        'vaccine': my_vaccine,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    return render(request, "vaccine/vaccine_form.html", context)


@login_required
@permission_required('vaccine.delete_vaccine', raise_exception=True)
def VaccineDelete(request, id_user, id_pet, id_vac):
    if request.method == 'POST':
        my_vaccine = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .vaccine_set.get(id=id_vac)

        my_vaccine.delete()
        return redirect('vaccine_list', id_user, id_pet)
    else:
        my_vaccine = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .vaccine_set.get(id=id_vac)

    context = {
        'form': VaccineForm(),
        'vaccine': my_vaccine,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    return render(request, 'vaccine/vaccine_confirm_delete.html', context)
