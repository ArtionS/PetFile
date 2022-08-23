from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pet(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    type_animal = models.CharField(max_length=500)
    raze = models.CharField(max_length=500)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=FEMALE,
    )
    description = models.TextField(null=True, blank=True)
    birth_day = models.DateField()
    picture = models.CharField(max_length=500, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)  # hace referencia de cuando de actualiza  (todo el tiempo)
    created = models.DateTimeField(auto_now_add=True)  # hace referencia a cuando se creo la mascota (una vez)

    # weight = models.ArrayField()    #List
    # vaccines  #List
    # rocess    #List

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
