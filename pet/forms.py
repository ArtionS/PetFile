from django.forms import ModelForm, TextInput
from .models import Pet


# Asignacion de los campos que se usaran para el formulario de la mascota
class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'type_animal',
            'raze',
            'gender',
            'description',
            'birth_day',
            'picture',
        ]
        widgets = {
            'name': TextInput(attrs={'required': True}),
        }



