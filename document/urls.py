from django.urls import path
from .views import DocumentList,\
    DocumentDetail, \
    DocumentCreate, \
    DocumentUpdate, \
    DocumentDelete

urlpatterns = [
    # URL's dedicadas a Usuarios y Admins
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/documents/', DocumentList, name='document_list'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/', DocumentDetail, name='document_detail'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/create/', DocumentCreate, name='document_create'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/update/', DocumentUpdate, name='document_update'),
    path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/delete/', DocumentDelete, name='document_delete'),
]
