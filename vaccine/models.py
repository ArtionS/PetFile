from django.db import models
from pet.models import Pet

# Create your models here.


class Vaccine(models.Model):
    pet_id = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    updated = models.DateTimeField(auto_now=True)  # hace referencia de cuando de actualiza  (todo el tiempo)
    created = models.DateTimeField(auto_now_add=True)  # hace referencia a cuando se creo la mascota (una vez)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name


