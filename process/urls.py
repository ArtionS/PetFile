from django.urls import path
from .views import ProcessList, \
    ProcessDetail, \
    ProcessCreate, \
    ProcessUpdate, \
    ProcessDelete

urlpatterns = [
    path('pet/<int:id_pet>/processes/', ProcessList.as_view(), name='process_list'),
    path('pet/<int:id_pet>/process/<int:id_pro>/', ProcessDetail.as_view(), name='process_detail'),
    path('pet/<int:id_pet>/process/create/', ProcessCreate.as_view(), name='process_create'),
    path('pet/<int:id_pet>/process/<int:id_pro>/update/', ProcessUpdate.as_view(), name='process_update'),
    path('pet/<int:id_pet>/process/<int:id_pro>/delete', ProcessDelete.as_view(), name='process_delete'),

]