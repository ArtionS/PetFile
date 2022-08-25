from django.shortcuts import render

# Paquete para pedir que se este en modo login
# from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProcessForm


def ProcessList(request, id_pet):
    context = {
        'processes': request.user.pet_set.get(id=id_pet).process_set.all(),
        'id_pet': id_pet
    }

    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['processes'] = context['processes'].filter(title__icontains=search_input)
        # context['processes'] = context['processes'].filter(title__startswith=search_input)
    context['search_input'] = search_input

    return render(request, "process/process_list.html", context)


def ProcessDetail(request, id_pet, id_pro):
    context = {
        'process' : request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro),
        'documents' : request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.all(),
        'id_pet' : id_pet
    }
    return render(request, "process/process_detail.html", context)


def ProcessCreate(request, id_pet):
    if request.method == 'POST':
        # print('Process Create Post')
        form = ProcessForm(request.POST, request.FILES)
        if form.is_valid():
            # print('Process Create Validate Create Post')
            form.instance.pet_id = request.user.pet_set.get(id=id_pet)
            form.save()
            return ProcessList(request, id_pet)
        else:
            print('/ No thanks/')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        print('Process Create GET')
        form = ProcessForm()
    return render(request, "process/process_form.html", {'form': form, 'id_pet': id_pet})


def ProcessUpdate(request, id_pet, id_pro):
    if request.method == 'POST':
        form = ProcessForm(request.POST, request.FILES)
        if form.is_valid():
            myprocess = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)

            myprocess.type_process = form['type_process'].value()
            myprocess.title = form['title'].value()
            myprocess.description = form['description'].value()
            myprocess.weight = form['weight'].value()

            myprocess.save()
            return ProcessList(request, id_pet)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        myprocess = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
        form = ProcessForm()
    return render(request, 'process/process_form.html', {'form': form, 'process': myprocess, 'id_pet': id_pet})


def ProcessDelete(request, id_pet, id_pro):
    if request.method == 'POST':
        myprocess = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
        myprocess.delete()
        return ProcessList(request, id_pet)
    # if a GET (or any other method) we'll create a blank form
    else:
        myprocess = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
        form = ProcessForm()
    return render(request, 'process/process_confirm_delete.html',
                  {'form': form, 'process': myprocess, 'id_pet': id_pet})
