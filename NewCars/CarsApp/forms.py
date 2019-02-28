from django import forms
from .models import ModelForm


class Userform(forms.ModelForm):
    class Meta:
        model = ModelForm
        fields = '__all__'
