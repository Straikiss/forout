from django import forms
from .import models

class CreatePack2(forms.ModelForm):
  class Meta:
    model = models.Pack2
    fields = ['slug', 'poster', 'video', 'time', 'size']