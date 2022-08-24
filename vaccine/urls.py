from django.urls import path
from .views import VaccineList, \
    VaccineDetail, \
    VaccineCreate, \
    VaccineUpdate, \
    VaccineDelete

urlpatterns = [
    path('pet/<int:id_pet>/vaccines/', VaccineList, name='vaccine_list'),
    path('pet/<int:id_pet>/vaccine/<int:id_vac>/', VaccineDetail, name='vaccine_detail'),
    path('pet/<int:id_pet>/vaccine/create/', VaccineCreate, name='vaccine_create'),
    path('pet/<int:id_pet>/vaccine/<int:id_vac>/update/', VaccineUpdate, name='vaccine_update'),
    path('pet/<int:id_pet>/vaccine/<int:id_vac>/delete', VaccineDelete, name='vaccine_delete'),

]
