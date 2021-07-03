from django.shortcuts import render, redirect
from .models import Videos
from .import forms
import cloudinary.uploader
import cloudinary


def index_videos(request):
  video = Videos.objects.count()
  videos = Videos.objects.all()
  return render(request, 'videos/videos.html', {'videos': videos, 'video': video})

def video_videos(request, slug):
  video = Videos.objects.get(slug=slug)
  videos = Videos.objects.all()
  return render(request, 'videos/video.html', {'videos': videos, 'video': video})

def upload_videos(request):
  if request.method == 'POST':
    form = forms.CreateVideos(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
  else:
    form = forms.CreateVideos()
  return render(request, 'videos/upload.html', {'form': form})

def delete_videos(request, slug):
  if request.method == 'POST':
    video = Videos.objects.get(slug=slug)
    poster = Videos.objects.get(slug=slug)
    cloudinary.uploader.destroy(video.video.public_id, resource_type='video')
    cloudinary.uploader.destroy(poster.poster.public_id, resource_type='image')
    instance = Videos.objects.get(slug=slug)
    instance.delete()
  return redirect('videos')