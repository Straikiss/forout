from django import forms
from .import models

class CreatePremium(forms.ModelForm):
  class Meta:
    model = models.Premium
    fields = ['slug', 'poster', 'video', 'time', 'size']