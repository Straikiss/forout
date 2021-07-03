from django.shortcuts import render, redirect
from .models import Pack3
from .import forms
import cloudinary.uploader
import cloudinary


def index_pack3(request):
  video = Pack3.objects.count()
  videos = Pack3.objects.all()
  return render(request, 'pack3/videos.html', {'videos': videos, 'video': video})

def video_pack3(request, slug):
  video = Pack3.objects.get(slug=slug)
  videos = Pack3.objects.all()
  return render(request, 'pack3/video.html', {'videos': videos, 'video': video})

def upload_pack3(request):
  if request.method == 'POST':
    form = forms.CreatePack3(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
  else:
    form = forms.CreatePack3()
  return render(request, 'pack3/upload.html', {'form': form})

def delete_pack3(request, slug):
  if request.method == 'POST':
    video = Pack3.objects.get(slug=slug)
    poster = Pack3.objects.get(slug=slug)
    cloudinary.uploader.destroy(video.video.public_id, resource_type='video')
    cloudinary.uploader.destroy(poster.poster.public_id, resource_type='image')
    instance = Pack3.objects.get(slug=slug)
    instance.delete()
  return redirect('pack3')