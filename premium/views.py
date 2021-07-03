from django.shortcuts import render, redirect
from .models import Premium
from .import forms
import cloudinary.uploader
import cloudinary


def index_premium(request):
  video = Premium.objects.count()
  videos = Premium.objects.all()
  return render(request, 'premium/videos.html', {'videos': videos, 'video': video})

def video_premium(request, slug):
  video = Premium.objects.get(slug=slug)
  videos = Premium.objects.all()
  return render(request, 'premium/video.html', {'videos': videos, 'video': video})

def upload_premium(request):
  if request.method == 'POST':
    form = forms.CreatePremium(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
  else:
    form = forms.CreatePremium()
  return render(request, 'premium/upload.html', {'form': form})

def delete_premium(request, slug):
  if request.method == 'POST':
    video = Premium.objects.get(slug=slug)
    poster = Premium.objects.get(slug=slug)
    cloudinary.uploader.destroy(video.video.public_id, resource_type='video')
    cloudinary.uploader.destroy(poster.poster.public_id, resource_type='image')
    instance = Premium.objects.get(slug=slug)
    instance.delete()
  return redirect('premium')