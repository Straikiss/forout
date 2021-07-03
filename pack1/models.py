from django.db import models
from cloudinary.models import CloudinaryField


class Pack1(models.Model):
  slug = models.SlugField()
  poster = CloudinaryField(resource_type='image', folder='pack1_poster/')
  video = CloudinaryField(resource_type='video', folder='pack1_video/')
  time = models.TextField(default='0:00')
  size = models.TextField(default='0')