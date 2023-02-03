from django import forms

from contatos.models import Contato

# from django.db import models


# Create your models here.
class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)
