from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# modelos para la creacion de la mascota


class Pet(models.Model):
    # asignaion  del dueño de la mascota
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # opciones para el seo de la mascota
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, blank=False, null=False)

    type_animal = models.CharField(max_length=500, blank=False, null=False)

    raze = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=FEMALE,
        blank=False, null=False
    )
    description = models.TextField(null=True, blank=True)
    birth_day = models.DateField(blank=False, null=False)
    # upload is a subdirectory created in MEDIA_ROOT o MEDIA_URL
    picture = models.ImageField(null=True, blank=True, upload_to="images/")

    updated = models.DateTimeField(auto_now=True)  # hace referencia de cuando de actualiza  (todo el tiempo)
    created = models.DateTimeField(auto_now_add=True)  # hace referencia a cuando se creo la mascota (una vez)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
