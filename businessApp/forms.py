from django import forms
from django.forms import ModelForm
from .models import businessApp



class businessAppForm(ModelForm):
    class Meta:
        model = businessApp
        fields = '__all__'
        # fields = ['task', 'a', 'b','c']
        print('\nfields: ', fields)