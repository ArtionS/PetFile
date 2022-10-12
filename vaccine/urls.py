from django.urls import path
from .views import VaccineList, \
    VaccineDetail, \
    VaccineCreate, \
    VaccineUpdate, \
    VaccineDelete

urlpatterns = [
    path('user/<int:id_user>/pet/<int:id_pet>/vaccines/', VaccineList, name='vaccine_list'),
    path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/', VaccineDetail, name='vaccine_detail'),
    path('user/<int:id_user>/pet/<int:id_pet>/vaccine/create/', VaccineCreate, name='vaccine_create'),
    path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/update/', VaccineUpdate, name='vaccine_update'),
    path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/delete/', VaccineDelete, name='vaccine_delete'),

]
