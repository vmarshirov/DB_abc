from django import forms
from django.forms import ModelForm
from .models import AbcModel



class AbcModelForm(ModelForm):
    class Meta:
        model = AbcModel
        fields = '__all__'
        # fields = ['task', 'a', 'b','c']
        print('\nfields: ', fields)