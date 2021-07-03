from django import forms
from .import models

class CreateVideos(forms.ModelForm):
  class Meta:
    model = models.Videos
    fields = ['slug', 'poster', 'video', 'time', 'size']