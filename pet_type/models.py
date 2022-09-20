from django.db import models

# Create your models here.


# modelos para los tipos de animales
class PetType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name