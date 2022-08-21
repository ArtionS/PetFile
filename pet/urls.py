from django.urls import path
from .views import PetList, PetDetail, PetCreate, PetUpdate, PetDelete


urlpatterns = [
    path('pets/', PetList.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('pet/create/', PetCreate.as_view(), name='pet_create'),
    path('pet/<int:pk>/update/', PetUpdate.as_view(), name='pet_update'),
    path('pet/<int:pk>/delete/', PetDelete.as_view(), name='pet_delete'),
]
