from django.shortcuts import render, redirect

# Paquete para pedir que se este en modo login y pedir permisos
# from django.contrib.auth.decorators import login_required , permission_required
# Create your views here.

# from django.contrib.auth.models import User

# Importacion de modelos de Usuario y de UsertoVet
from .models import ConectionUV
from django.contrib.auth.models import User

"""
Bloque de funciones para Usuarios
"""


def UserList(request):
    con = ConectionUV.objects.filter(user_id=request.user)

    context = {
        "users": con[0].vets.all()
    }

    return render(request, "veterinary/user_list.html", context)


def UserDetail(request, id_user):
    con = ConectionUV.objects.filter(user_id=request.user)
    user = con[0].vets.get(id=id_user)
    pets = user.pet_set.all()

    context = {
        "user": user,
        "pets": pets,
    }
    return render(request, "veterinary/user_detail.html", context)

"""
Bloque de funciones para las Mascotas de Usuarios
"""


def UserPetDetail(request, id_user, id_pet):
    con = ConectionUV.objects.filter(user_id=request.user)
    user = con[0].vets.get(id=id_user)
    pet = user.pet_set.get(id=id_pet)

    context = {
        "user": user,
        "pet": pet,
    }
    return render(request, "veterinary/user_pet_detail.html", context)

"""
Bloque de Funciones para Veterinarios
"""


# Funciones para a muestra de los veterinarios a los usuarios
def VetList(request):
    con = ConectionUV.objects.filter(user_id=request.user)

    if len(con) == 0:
        vets = {}
    else:
        vets = con[0].vets.all()

    context = {
        "vets": vets
    }

    return render(request, "veterinary/vet_list.html", context)


def VetDetail(request, id_vet):
    """
    Parte pendiente para desarrollo en la nuve QR
    """

    if request.user.groups.filter(name='group_vet').exists():
        vet = request.user

    if request.user.groups.filter(name='group_user').exists():
        con = ConectionUV.objects.filter(user_id=request.user)
        if len(con) == 0:
            vet = {}
        else:
            vet = con[0].vets.get(id=id_vet)

    print("Prueba de URL para QR")
    link = f"http://{request.get_host()}/veterinary/create/{id_vet}/"
    print(link)

    context = {
        "vet": vet,
        "link" : link,
    }
    return render(request, "veterinary/vet_detail.html", context)


def VetCreate(request, id_vet):
    # print("Actual")
    # actual_conection_user = ConectionUV.objects.filter(user_id=request.user)
    if len(ConectionUV.objects.filter(user_id=id_vet)) == 0:
        new_conection = ConectionUV(user_id=User.objects.get(id=id_vet))
        new_conection.save()

    if len(ConectionUV.objects.filter(user_id=request.user)) == 0:
        new_conection = ConectionUV(user_id=request.user)
        new_conection.save()

    print("Vets")
    vet_conection = ConectionUV.objects.filter(user_id=id_vet)
    print(vet_conection)
    print(vet_conection[0].vets.all())

    print("User")
    user_conection = ConectionUV.objects.filter(user_id=request.user)
    print(user_conection)
    print(user_conection[0].vets.all())

    context = {
        "vet": User.objects.get(id=id_vet)
    }

    if request.user in vet_conection[0].vets.all():
        print("Si")
        return render(request, "veterinary/conection_ready.html", context)

    print("No")

    if request.method == 'POST':
        print("Register")
        user_conection[0].vets.add(User.objects.get(id=id_vet))
        vet_conection[0].vets.add(request.user)
        return redirect('vet_create', id_vet)

    return render(request, "veterinary/conection.html", context)


def VetDelete(request, id_vet):
    """
    Proceso para la quitar a un veterinario de la lista de veterinarios de un usuario
    y
    Proceso para quitar de la lista de usuarios a un Usuario

    Ambos deben de estar en las listas del otro y se procedera a eliminarlos de
    """
    # validacion de que el veterinario tenga su lista de conecciones
    if len(ConectionUV.objects.filter(user_id=id_vet)) == 0:
        new_conection = ConectionUV(user_id=User.objects.get(id=id_vet))
        new_conection.save()

    # validacion de que el usuario tenga su lista de conecciones
    if len(ConectionUV.objects.filter(user_id=request.user)) == 0:
        new_conection = ConectionUV(user_id=request.user)
        new_conection.save()

    # conecciones del veterinari
    vet_conection = ConectionUV.objects.filter(user_id=id_vet)
    # conecciones del usuario
    user_conection = ConectionUV.objects.filter(user_id=request.user)

    context = {
        "vet": User.objects.get(id=id_vet)
    }

    # Validacion de que el usuario NO este en la lista del veterinari
    if request.user not in vet_conection[0].vets.all():
        return render(request, "veterinary/vet_ready_delete.html", context)

    if request.method == 'POST':
        user_conection[0].vets.remove(User.objects.get(id=id_vet))
        vet_conection[0].vets.remove(request.user)
        return redirect('vet_delete', id_vet)

    return render(request, "veterinary/vet_confirm_delete.html", context)
