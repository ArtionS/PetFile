from django.urls import path

from .views import VetList, VetDetail, VetCreate, VetDelete, \
    UserList, UserDetail, UserPetDetail

    # UserPetUpdate, UserPetDelete, \
    # UserPetVaccineDetail, UserPetVaccineCreate, UserPetVaccineUpdate, UserPetVaccineDelete, \
    # UserPetProcessDetail, UserPetProcessCreate, UserPetProcessUpdate, UserPetProcessDelete, \
    # UserPetProcessDocumentDetail, UserPetProcessDocumentCreate, UserPetProcessDocumentUpdate, \
    # UserPetProcessDocumentDelete

# from django.contrib.auth.views import LogoutView

urlpatterns = [
    # URLs veterinary
    path('veterinarys/', VetList, name='vet_list'),
    path('veterinary/<int:id_vet>/', VetDetail, name='vet_detail'),
    path('veterinary/create/<int:id_vet>/', VetCreate, name='vet_create'),
    path('veterinary/<int:id_vet>/delete/', VetDelete, name='vet_delete'),

    # URLs Users
    path('users/', UserList, name='user_list'),
    path('user/<int:id_user>/', UserDetail, name='user_detail'),

    # URLs Pet
    path('user/<int:id_user>/pet/<int:id_pet>/', UserPetDetail, name='user_pet_detail'),

    # path('user/<int:id_user>/pet/create/', UserPetCreate, name='user_pet_create'),
    # path('user/<int:id_user>/pet/<int:id_pet>/update/', UserPetUpdate, name='user_pet_update'),
    # path('user/<int:id_user>/pet/<int:id_pet>/delete/', UserPetDelete, name='user_pet_delete'),
    #
    # # URLs Vaccines
    # path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/',
    #      UserPetVaccineDetail, name='user_pet_vaccine_detail'),
    # path('user/<int:id_user>/pet/<int:id_pet>/vaccine/create/',
    #      UserPetVaccineCreate, name='user_pet_vaccine_create'),
    # path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/update/',
    #      UserPetVaccineUpdate, name='user_pet_vaccine_update'),
    # path('user/<int:id_user>/pet/<int:id_pet>/vaccine/<int:id_vac>/delete/',
    #      UserPetVaccineDelete, name='user_pet_vaccine_delete'),
    #
    # # URLs Process
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/',
    #      UserPetProcessDetail, name='user_pet_process_detail'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/create/',
    #      UserPetProcessCreate, name='user_pet_process_create'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/update/',
    #      UserPetProcessUpdate, name='user_pet_process_update'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/delete/',
    #      UserPetProcessDelete, name='user_pet_process_delete'),
    #
    # # URLs Documents
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/',
    #      UserPetProcessDocumentDetail, name='user_pet_process_document_detail'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/create/',
    #      UserPetProcessDocumentCreate, name='user_pet_process_document_create'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/update/',
    #      UserPetProcessDocumentUpdate, name='user_pet_process_document_update'),
    # path('user/<int:id_user>/pet/<int:id_pet>/process/<int:id_pro>/document/<int:id_doc>/delete/',
    #      UserPetProcessDocumentDelete, name='user_pet_process_document_delete'),

]
