from django.shortcuts import render, redirect


# Paquete para pedir que se este en modo login y pedir permisos
# from django.contrib.auth.decorators import login_required , permission_required
# Create your views here.




def VetList(request):
    context = {"hey" : 14}
    return render(request, "veterinary/vet_list.html", context)


def VetDetail(request, id_vet):
    context = {"hey": 14}
    return render(request, "veterinary/vet_detail.html", context)


def VetCreate(request, id_vet):
    context = {"hey": 14}
    return render(request, "veterinary/vet_form.html", context)


def VetDelete(request, id_vet):
    context = {"hey": 14}
    return render(request, "veterinary/vet_confirm_delete.html", context)
