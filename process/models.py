from django.db import models
from pet.models import Pet

# Create your models here.


class Process(models.Model):
    CONSULT = 'C'
    PROCESS = 'P'
    PROCESS_CHOICES = [
        (CONSULT, 'Consult'),
        (PROCESS, 'Process'),
    ]

    pet_id = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    id = models.AutoField(primary_key=True)
    type_process = models.CharField(
        max_length=2,
        choices=PROCESS_CHOICES,
        default=CONSULT,
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    updated = models.DateTimeField(auto_now=True)  # hace referencia de cuando de actualiza  (todo el tiempo)
    created = models.DateTimeField(auto_now_add=True)  # hace referencia a cuando se creo la mascota (una vez)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.title


