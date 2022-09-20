from django.forms import ModelForm
from .models import Process


# creacion del modelo de los porcesos
class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = [
            'type_process',
            'title',
            'description',
            'weight',
        ]
