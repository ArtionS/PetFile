from django.urls import path
from .views import PetList, PetDetail, PetCreate, PetUpdate, PetDelete


urlpatterns = [
    path('pets/', PetList, name='pet_list'),
    path('pet/<int:pk>/', PetDetail, name='pet_detail'),

    path('user/<int:id_user>/pet/create/', PetCreate, name='pet_create'),
    path('user/<int:id_user>/pet/<int:id_pet>/update/', PetUpdate, name='pet_update'),
    path('pet/<int:pk>/delete/', PetDelete, name='pet_delete'),
]
