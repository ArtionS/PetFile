from django.forms import ModelForm
from .models import Pet


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
