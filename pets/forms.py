from typing import Any
from django import forms
from pets.models import Pet

class PetModelForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
    
