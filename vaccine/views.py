from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# @login_required()

from .forms import VaccineForm

@login_required()
def VaccineList(request, id_pet):
    context = {
        'vaccines': request.user.pet_set.get(id=id_pet).vaccine_set.all(),
        'id_pet': id_pet
    }

    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['vaccines'] = context['vaccines'].filter(name__icontains=search_input)
        # context['processes'] = context['processes'].filter(title__startswith=search_input)
    context['search_input'] = search_input

    return render(request, "vaccine/vaccine_list.html", context)

@login_required()
def VaccineDetail(request, id_pet, id_vac):
    context = {
        'vaccine': request.user.pet_set.get(id=id_pet).vaccine_set.get(id=id_vac),
        'id_pet': id_pet
    }
    return render(request, "vaccine/vaccine_detail.html", context)

@login_required()
def VaccineCreate(request, id_pet):
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.pet_id = request.user.pet_set.get(id=id_pet)
            form.save()
            return VaccineList(request, id_pet)
        else:
            print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VaccineForm()
    return render(request, "vaccine/vaccine_form.html", {'form': form, 'id_pet': id_pet})

@login_required()
def VaccineUpdate(request, id_pet, id_vac):
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            myvaccine = request.user.pet_set.get(id=id_pet).vaccine_set.get(id=id_vac)

            myvaccine.name = form['name'].value()

            myvaccine.save()
            return VaccineList(request, id_pet)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        myvaccine = request.user.pet_set.get(id=id_pet).vaccine_set.get(id=id_vac)
        form = VaccineForm()
    return render(request, 'process/process_form.html', {'form': form, 'vaccine': myvaccine, 'id_pet': id_pet})

@login_required()
def VaccineDelete(request, id_pet, id_vac):
    if request.method == 'POST':
        myvaccine = request.user.pet_set.get(id=id_pet).vaccine_set.get(id=id_vac)
        myvaccine.delete()
        return VaccineList(request, id_pet)
    else:
        myvaccine = request.user.pet_set.get(id=id_pet).vaccine_set.get(id=id_vac)
        form = VaccineForm()
    return render(request, 'vaccine/vaccine_confirm_delete.html' ,
                  {'form' : form , 'vaccine' : myvaccine , 'id_pet' : id_pet})

