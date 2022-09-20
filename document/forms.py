from django.forms import ModelForm
from .models import Document


# creacion del formulario
class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = [
            'name',
            'document'
        ]
