from django.shortcuts import render, redirect

from .forms import DocumentForm
from process.views import ProcessDetail
# Create your views here.


def DocumentList(request, id_pet, id_pro):
    context = {'id_pet': id_pet, 'id_pro': id_pro}
    return redirect(request, 'process/process_detail', context)


def DocumentDetail(request, id_pet, id_pro, id_doc):
    context = {
        'id_pet' : id_pet,
        'id_pro' : id_pro,
        'document': request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.get(id=id_doc),
    }
    return render(request , 'document/document_detail.html', context)


def DocumentCreate(request, id_pet, id_pro):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.pro_id = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
            form.save()
            # mydoc = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
            # return render(request, 'process/process_detail.html', {'id_pet': id_pet, 'id_pro': id_pro, 'process' : mypro })
            # return DocumentDetail(request,  id_pet,  id_pro , mydoc.id)
            # return ProcessDetail(request, id_pet , id_pro)
            return redirect('document_detail' , id_pet , id_pro , form.instance.id)
        else:
            print('/ No thanks/')
            print(form.errors)
    else:
        form = DocumentForm()
    return render(request, 'document/document_form.html', {'form': form, 'id_pet': id_pet, 'id_pro': id_pro})


def DocumentUpdate(request, id_pet, id_pro, id_doc):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            mydocument = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.get(id=id_doc)

            mydocument.name = form['name'].value()
            mydocument.document = form['document'].value()
            mydocument.save()

            return redirect('document_detail' , id_pet , id_pro , mydocument.id)
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        mydocument = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.get(id=id_doc)
        form = DocumentForm()
    return render(request, 'document/document_form.html',
                  {'form': form, 'document': mydocument, 'id_pet': id_pet, 'id_pro': id_pro})



def DocumentDelete(request, id_pet, id_pro, id_doc):
    if request.method == 'POST':
        mydocument = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.get(id=id_doc)
        mydocument.delete()
        return redirect('process_detail' , id_pet , id_pro)
    # if a GET (or any other method) we'll create a blank form
    else:
        mydocument = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro).document_set.get(id=id_doc)
        form = DocumentForm()
    return render(request, 'document/document_confirm_delete.html',
                  {'form': form, 'document': mydocument, 'id_pet': id_pet, 'id_pro': id_pro})
