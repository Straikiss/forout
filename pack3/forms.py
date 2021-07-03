from django import forms
from .import models

class CreatePack3(forms.ModelForm):
  class Meta:
    model = models.Pack3
    fields = ['slug', 'poster', 'video', 'time', 'size']