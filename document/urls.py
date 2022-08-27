from django.urls import path
from .views import DocumentList,\
    DocumentDetail, \
    DocumentCreate, \
    DocumentUpdate, \
    DocumentDelete

urlpatterns = [
    path('pet/<int:id_pet>/process/<int:id_pro>/documents/', DocumentList, name='document_list'),
    path('pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/', DocumentDetail, name='document_detail'),
    path('pet/<int:id_pet>/process/<int:id_pro>/document/create/', DocumentCreate, name='document_create'),
    path('pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/update/', DocumentUpdate, name='document_update'),
    path('pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/delete/', DocumentDelete, name='document_delete'),
]
