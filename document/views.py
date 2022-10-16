from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required

# @login_required
# @permission_required('vaccine.view_vaccine', raise_exception=True)

"""
Import the Form Tp Create an Edit Documents
"""
from .forms import DocumentForm

"""
Importacion el modelo de coneccion para asignacion de dueño a la mascota
"""
from veterinary.models import ConectionUV


# funcion para mostrar lista de docuemntos
@login_required
@permission_required('document.view_document', raise_exception=True)
def DocumentList(request, id_pet, id_pro):
    context = {
        'id_pet': id_pet,
        'id_pro': id_pro
    }
    return redirect(request, 'process/process_detail', context)


# Funcion para los detalles de un documento
@login_required
@permission_required('document.view_document', raise_exception=True)
def DocumentDetail(request, id_user, id_pet, id_pro, id_doc):
    # Document List
    document = {}
    """
    Validar si es usuario o veterinario
    """
    if request.user.groups.filter(name='group_vet').exists():
        document = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.get(id=id_doc)

    if request.user.groups.filter(name='group_user').exists():
        document = request.user.pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.get(id=id_doc)

    context = {
        'document': document,
        'id_user': id_user,
        'id_pet': id_pet,
        'id_pro': id_pro,
    }
    return render(request, 'document/document_detail.html', context)


# Funcion para crear un documento nuevo
@login_required
@permission_required('document.add_document', raise_exception=True)
def DocumentCreate(request, id_user, id_pet, id_pro):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() and request.user.groups.filter(name='group_vet').exists():

            form.instance.pro_id = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)\
                .process_set.get(id=id_pro)

            # form.instance.pro_id = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
            form.save()
            return redirect('document_detail', id_user, id_pet, id_pro, form.instance.id)
        else:
            print('/ No thanks/')
            print(form.errors)
    else:
        form = DocumentForm()

    context = {
        'form': form,
        'id_user': id_user,
        'id_pet': id_pet,
        'id_pro': id_pro,
    }
    return render(request, 'document/document_form.html', context)


# Funcion para Actualizar un doumento
@login_required
@permission_required('document.change_document', raise_exception=True)
def DocumentUpdate(request, id_user, id_pet, id_pro, id_doc):
    my_document = {}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            my_document = ConectionUV.objects.filter(user_id=request.user)[0]\
                .vets.get(id=id_user)\
                .pet_set.get(id=id_pet)\
                .process_set.get(id=id_pro)\
                .document_set.get(id=id_doc)

            my_document.name = form['name'].value()

            if form['document'].value():
                my_document.document = form['document'].value()

            my_document.save()
            return redirect('document_detail', id_user, id_pet, id_pro, my_document.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        my_document = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.get(id=id_doc)

    context = {
        'form': DocumentForm(),
        'document': my_document,
        'id_user': id_user,
        'id_pet': id_pet,
        'id_pro': id_pro,
    }
    return render(request, 'document/document_form.html', context)


# Funcion para eliminar un documento
@login_required
@permission_required('document.delete_document', raise_exception=True)
def DocumentDelete(request, id_user, id_pet, id_pro, id_doc):
    if request.method == 'POST':
        my_document = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.get(id=id_doc)

        my_document.delete()
        return redirect('process_detail', id_user, id_pet, id_pro)
    # if a GET (or any other method) we'll create a blank form
    else:
        my_document = ConectionUV.objects.filter(user_id=request.user)[0]\
            .vets.get(id=id_user)\
            .pet_set.get(id=id_pet)\
            .process_set.get(id=id_pro)\
            .document_set.get(id=id_doc)
        form = DocumentForm()

    context = {
        'form': form,
        'document': my_document,
        'id_user': id_user,
        'id_pet': id_pet,
        'id_pro': id_pro,
    }
    return render(request, 'document/document_confirm_delete.html', context)
