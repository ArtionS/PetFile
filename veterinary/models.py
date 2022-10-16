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
