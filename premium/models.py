from django.db import models
from cloudinary.models import CloudinaryField


class Premium(models.Model):
  slug = models.SlugField()
  poster = CloudinaryField(resource_type='image', folder='premium_poster/')
  video = CloudinaryField(resource_type='video', folder='premium_video/')
  time = models.TextField(default='0:00')
  size = models.TextField(default='0')