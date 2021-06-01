
from django import forms

from .models import *


class matriculaObsForm(forms.ModelForm):
    class Meta:
        model = matricula
        fields = ['observacoes']


