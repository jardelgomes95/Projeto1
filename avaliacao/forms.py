from django import forms

from .models import avaliacao, objetivos, ficha_de_saude, medicamento, nutricao


class avaliacaoObsForm(forms.ModelForm):
    class Meta:
        model = avaliacao
        fields = ['observacoes']



class ficha_de_saudeObsForm(forms.ModelForm):
    class Meta:
        model = ficha_de_saude
        fields = ['observacoes']


class objetivosObsForm(forms.ModelForm):
    class Meta:
        model = objetivos
        fields = ['observacoes']


class medicamentoObsForm(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = ['observacoes']


class nutricaoObsForm(forms.ModelForm):
    class Meta:
        model = nutricao
        fields =['observacoes']

