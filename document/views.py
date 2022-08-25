from django.shortcuts import render

from .forms import DocumentForm
from process.views import ProcessDetail
# Create your views here.


def DocumentDetail(request, id_pet, id_pro, id_doc):

    render()


def DocumentCreate(request, id_pet, id_pro):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.pro_id = request.user.pet_set.get(id=id_pet).process_set.get(id=id_pro)
            form.save()
            return ProcessDetail(request,  id_pet,  id_pro)
        else:
            print('/ No thanks/')
            print(form.errors)
    else:
        form = DocumentForm
    return render(request, 'document/document_form.html', {'form': form, 'id_pet': id_pet, 'id_pro': id_pro})


def DocumentUpdate(request, id_pet, id_pro, id_doc):
    render()


def DocumentDelete(request, id_pet, id_pro, id_doc):

    render()