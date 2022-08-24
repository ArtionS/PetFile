from django.urls import path
from .views import ProcessList, \
    ProcessDetail, \
    ProcessCreate, \
    ProcessUpdate, \
    ProcessDelete

urlpatterns = [
    path('pet/<int:id_pet>/processes/', ProcessList, name='process_list'),
    path('pet/<int:id_pet>/process/<int:id_pro>/', ProcessDetail, name='process_detail'),
    path('pet/<int:id_pet>/process/create/', ProcessCreate, name='process_create'),
    path('pet/<int:id_pet>/process/<int:id_pro>/update/', ProcessUpdate, name='process_update'),
    path('pet/<int:id_pet>/process/<int:id_pro>/delete', ProcessDelete, name='process_delete'),

]