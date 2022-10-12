from django.db import models
from django.contrib.auth.models import User


class ConectionUV(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_id')
    vets = models.ManyToManyField(User,  related_name='vets', blank=True)

    def __str__(self):
        return self.user_id.username

    def add(self, account):
        """
        Add new Vet
        """
        if not account in self.vets.all():
            self.vets.add(account)
            self.save()

    def remove(self, account):
        """
        Remove a Vet
        """
        if account in self.vets.all():
            self.vets.remuve(account)


    def stop_share_data(self, vet):
        """
        Initiate the action of delete and stop share the data with a vet
        """
        remover_vet_list = self # user unlinking from the vet

        # Remove Vet from User vet list
        remover_vet_list.remove(vet)

        # Remove User from Vet user list
        user_list = ConectionUV.objects.get(user=vet)
        user_list.remove(self.user_id)

    def is_conection_redy(self, vet):
        """
        is this vet is in my Vet list?
        """
        if vet in self.vets.all():
            return True
        return False


# class VetRequest(models.Model):
#     """
#     Vet request
#     This request consists of two main parts
#         1. User sender
#         2. User Receiver
#     """
#
#     user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_sender")
#     user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_receiver")
#
#     is_active = models.BooleanField(blank=True, null=False, default=True)
#
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user_sender.username
#
#     def accept(self):
#         """
#         Accept to share the information
#         Update both User and Vet list
#         """
#         user_receiver_list = ConectionUV.objects.get(user=self.user_receiver)
#         if user_receiver_list:
#             user_receiver_list.add(self.user_sender)
#             user_sender_list = ConectionUV.objects.get(user=self.user_sender)
#             if user_sender_list:
#                 user_sender_list.add(self.user_receiver)
#                 self.is_active = False
#                 self.save()
#
#     def cancel(self):
#         """
#         cancel sharing the information
#         """
#         self.is_active = False
#         self.save()















