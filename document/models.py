from django.db import models
from process.models import Process


# Create your models here.


class Document(models.Model):
    pro_id = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    document = models.FileField(null=True, blank=True, upload_to="documents/")

    updated = models.DateTimeField(auto_now=True)  # hace referencia de cuando de actualiza todo el tiempo
    created = models.DateTimeField(auto_now_add=True)  # hace referencia a cuando se creo la mascota (una vez)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
