from django.db import models
from pet.models import Pet

# Create your models here.


class PetType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name