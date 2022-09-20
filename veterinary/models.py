from django.db import models
from django.contrib.auth.models import User


class UserToVet(models.Model):
    current_user = models.ManyToManyField(User)
    vet_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def add_vet(cls, current_user, current_vet):
        vetclient, created = cls.objects.get_or_create(
            current_user=current_user
        )
        vetclient.vet_user.add(current_vet)

    @classmethod
    def delete_vet(cls, current_user, current_vet):
        vetclient, created = cls.objects.get_or_create(
            current_user=current_user
        )
        vetclient.vet_user.remove(current_vet)

