from django.shortcuts import render , redirect

# Se importa
from django.contrib.auth.decorators import login_required , permission_required
# @login_required
# @permission_required('pet.view_pet', raise_exception=True)

"""
Import the Form Tp Create an Edit Process
"""
from .forms import ProcessForm

"""
Importacion el modelo de coneccion para asignacion de dueño a la mascota
"""
from veterinary.models import ConectionUV


@login_required
@permission_required('process.view_process', raise_exception=True)
def ProcessList(request, id_user, id_pet):
    # lista de procesos
    processes = {}
    """
    Validar si es usuario o veterinario
    """
    if request.user.groups.filter(name='group_vet').exists():
        processes = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.all()

    if request.user.groups.filter(name='group_user').exists():
        processes = request.user\
            .pet_set.get(id=id_pet)\
            .process_set.all()

    context = {
        'processes': processes,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['processes'] = context['processes'].filter(title__icontains=search_input)
        # context['processes'] = context['processes'].filter(title__startswith=search_input)
    context['search_input'] = search_input

    return render(request, "process/process_list.html", context)


@login_required
@permission_required('process.view_process', raise_exception=True)
def ProcessDetail(request, id_user, id_pet, id_pro):
    # lista de procesos
    process = {}
    documents = {}
    """
    Validar si es usuario o veterinario
    """
    if request.user.groups.filter(name='group_vet').exists():
        process = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)

        documents = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.all()

    if request.user.groups.filter(name='group_user').exists():
        process = request.user\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)

        documents = request.user\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.all()

    context = {
        'process' : process,
        'documents' : documents,
        'id_user': id_user,
        'id_pet' : id_pet,
    }
    return render(request, "process/process_detail.html", context)


@login_required
@permission_required('process.add_process', raise_exception=True)
def ProcessCreate(request, id_user, id_pet):
    context = {}
    if request.method == 'POST':
        form = ProcessForm(request.POST, request.FILES)
        if form.is_valid() and request.user.groups.filter(name='group_vet').exists():

            form.instance.pet_id = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)

            form.save()

            return redirect('process_detail', id_user, id_pet, form.instance.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'form': ProcessForm(),
            'id_user': id_user,
            'id_pet': id_pet,
        }
    return render(request, "process/process_form.html", context)


@login_required
@permission_required('process.change_process', raise_exception=True)
def ProcessUpdate(request, id_user, id_pet, id_pro):
    my_process = {}
    if request.method == 'POST':
        form = ProcessForm(request.POST, request.FILES)
        if form.is_valid() and request.user.groups.filter(name='group_vet').exists():

            my_process = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)\
                .process_set.get(id=id_pro)

            my_process.type_process = form['type_process'].value()
            my_process.title = form['title'].value()
            my_process.description = form['description'].value()
            my_process.weight = form['weight'].value()
            my_process.save()

            return redirect('process_detail', id_user, id_pet, my_process.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        my_process = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)

        form = ProcessForm()

    context = {
        'form': form,
        'process': my_process,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    return render(request, 'process/process_form.html', context)


@login_required
@permission_required('process.delete_process', raise_exception=True)
def ProcessDelete(request, id_user, id_pet, id_pro):
    if request.method == 'POST':
        my_process = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)

        my_process.delete()
        return redirect('process_list', id_user, id_pet)
    # if a GET (or any other method) we'll create a blank form
    else:
        my_process = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)

        form = ProcessForm()

    context = {
        'form': form,
        'process': my_process,
        'id_user': id_user,
        'id_pet': id_pet,
    }
    return render(request, 'process/process_confirm_delete.html', context)
