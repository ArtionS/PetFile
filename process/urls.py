from django.urls import path
from .views import ProcessList, \
    ProcessDetail, \
    ProcessCreate, \
    ProcessUpdate, \
    ProcessDelete

urlpatterns = [
    path('user/<int:id_user>/pet/<int:id_pet>/processes/', ProcessList, name='process_list'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/', ProcessDetail, name='process_detail'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/create/', ProcessCreate, name='process_create'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/update/', ProcessUpdate, name='process_update'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/delete', ProcessDelete, name='process_delete'),
]