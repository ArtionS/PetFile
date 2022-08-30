from django.shortcuts import render

# Create your views here.


def home_page(request):

    # print("Permisos PET")
    # print("create")
    # print(request.user.has_perm('pet.add_pet'))
    # print("update")
    # print(request.user.has_perm('pet.change_pet'))
    # print("delete")
    # print(request.user.has_perm('pet.delete_pet'))
    # print("detail")
    # print(request.user.has_perm('pet.view_pet'))


    return render(request, 'page/home_page.html')


def about_page(request):
    return render(request, 'page/about.html')
