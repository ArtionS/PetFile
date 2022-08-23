from django.urls import path
from .views import PetList, PetDetail, PetCreate, PetUpdate, PetDelete


urlpatterns = [
    path('pets/', PetList, name='pet_list'),
    path('pet/<int:pk>/', PetDetail, name='pet_detail'),
    path('pet/create/', PetCreate, name='pet_create'),
    path('pet/<int:pk>/update/', PetUpdate, name='pet_update'),
    path('pet/<int:pk>/delete/', PetDelete.as_view(), name='pet_delete'),
]
