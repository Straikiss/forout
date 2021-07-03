from django import forms
from .import models

class CreatePack1(forms.ModelForm):
  class Meta:
    model = models.Pack1
    fields = ['slug', 'poster', 'video', 'time', 'size']