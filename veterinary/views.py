from django.shortcuts import render, redirect


# Paquete para pedir que se este en modo login y pedir permisos
# from django.contrib.auth.decorators import login_required , permission_required
# Create your views here.

# from django.contrib.auth.models import User

# Importacion de modelos de Usuario y de UsertoVet
from .models import ConectionUV
from django.contrib.auth.models import User



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


# def UserPetDetail(request, id_user, id_pet):
#
#     user = User.objects.get(id=id_user)
#
#     pet = user.pet_set.get(id=id_pet)
#
#     # pets = Pet.objects.filter(owner=id_user)
#     # print(pet.__dict__)
#
#     context = {
#         "user": user,
#         "pet": pet,
#     }
#     return render(request, "veterinary/user_pet_detail.html", context)


# Funciones para a muestra de los veterinarios a los usuarios
def VetList(request):

    con = ConectionUV.objects.filter(user_id=request.user)

    # vets = con[0].vets.all()
    # for vet in vets:
    #     print(vet.__dict__)
    #     print(vet)

    context = {
        "vets": con[0].vets.all()
    }

    return render(request, "veterinary/vet_list.html", context)


def VetDetail(request, id_vet):
    con = ConectionUV.objects.filter(user_id=request.user)
    context = {
        "vet": con[0].vets.get(id=id_vet)
        # "vet": request.user.usertovet_set.get(vet_user=id_vet)
    }
    return render(request, "veterinary/vet_detail.html", context)


def VetCreate(request, id_vet):

    print("Actual")
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

    A,bos deben de estr en las listas del otro y se procedera a eliminarlos de
    """
    print("Actual")

    # validacion de que el veterinario tenga su lista de conecciones
    if len(ConectionUV.objects.filter(user_id=id_vet)) == 0:
        new_conection = ConectionUV(user_id=User.objects.get(id=id_vet))
        new_conection.save()

    # validacion de que el usuario tenga su lista de conecciones
    if len(ConectionUV.objects.filter(user_id=request.user)) == 0:
        new_conection = ConectionUV(user_id=request.user)
        new_conection.save()

    # Muestra de informacion de conecciones del veterinario
    print("Vets")
    vet_conection = ConectionUV.objects.filter(user_id=id_vet)
    print(vet_conection)
    print(vet_conection[0].vets.all())

    # Muestra de informacion de conecciones del usuario
    print("User")
    user_conection = ConectionUV.objects.filter(user_id=request.user)
    print(user_conection)
    print(user_conection[0].vets.all())

    context = {
        "vet": User.objects.get(id=id_vet)
    }

    # Validacion de que el usuario NO este en la lista del veterinari4
    # 5o
    if request.user not in vet_conection[0].vets.all():
        print("Si, No existe la coneccion ")
        return render(request, "veterinary/vet_ready_delete.html", context)

    print("No, Aun existe la coneccion")

    if request.method == 'POST':
        print("DELETION OF THE CONNECTION")
        user_conection[0].vets.remove(User.objects.get(id=id_vet))
        vet_conection[0].vets.remove(request.user)
        return redirect('vet_delete', id_vet)


    return render(request, "veterinary/vet_confirm_delete.html", context)

