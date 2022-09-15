from django.shortcuts import render, redirect


# Paquete para pedir que se este en modo login y pedir permisos
# from django.contrib.auth.decorators import login_required , permission_required
# Create your views here.

# from django.contrib.auth.models import User

from .models import UserToVet


def UserList(request):
    users = []

    user_list = UserToVet.objects.filter(vet_user_id=request.user.id)

    for userx in user_list:
        us = userx.current_user.all()
        for u in us:
            users.append(u)

    context = {
        "users" : users
    }

    return render(request, "veterinary/user_list.html", context)


def VetList(request):

    context = {
        "vets": request.user.usertovet_set.all()
    }
    return render(request, "veterinary/vet_list.html", context)


def VetDetail(request, id_vet):
    context = {
        "vet": request.user.usertovet_set.get(vet_user=id_vet)
    }
    return render(request, "veterinary/vet_detail.html", context)


def VetCreate(request, id_vet):
    context = {"hey": 14}
    return render(request, "veterinary/vet_form.html", context)


def VetDelete(request, id_vet):
    vet = request.user.usertovet_set.get(vet_user=id_vet)

    if request.method == 'POST':
        vet.delete()
        return redirect('vet_list')
    else:
        return render(request, "veterinary/vet_confirm_delete.html", {'vet': vet})




