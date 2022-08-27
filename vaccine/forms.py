from django.forms import ModelForm
from .models import Vaccine


class VaccineForm(ModelForm):
    class Meta:
        model = Vaccine
        fields = [
            'name',
        ]
