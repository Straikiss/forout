from django.db import models
from cloudinary.models import CloudinaryField


class Videos(models.Model):
  slug = models.SlugField()
  poster = CloudinaryField(resource_type='image', folder='videos_poster/')
  video = CloudinaryField(resource_type='video', folder='videos_video/')
  time = models.TextField(default='0:00')
  size = models.TextField(default='0')