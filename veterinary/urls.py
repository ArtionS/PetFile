from django.urls import path


from .views import VetList, VetDetail, VetCreate, VetDelete, UserList, UserDetail


# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('veterinarys/', VetList, name='vet_list'),
    path('veterinary/<int:id_vet>/', VetDetail, name='vet_detail'),
    path('veterinary/create/<int:id_vet>/', VetCreate, name='vet_create'),
    path('veterinary/<int:id_vet>/delete/', VetDelete, name='vet_delete'),

    path('users/', UserList, name='user_list'),
    path('user/<int:id_user>', UserDetail, name='user_detail'),
]
