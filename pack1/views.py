from django.shortcuts import render, redirect
from .models import Pack1
from .import forms
import cloudinary.uploader
import cloudinary


def index_pack1(request):
  video = Pack1.objects.count()
  videos = Pack1.objects.all()
  return render(request, 'pack1/videos.html', {'videos': videos, 'video': video})

def video_pack1(request, slug):
  video = Pack1.objects.get(slug=slug)
  videos = Pack1.objects.all()
  return render(request, 'pack1/video.html', {'videos': videos, 'video': video})

def upload_pack1(request):
  if request.method == 'POST':
    form = forms.CreatePack1(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
  else:
    form = forms.CreatePack1()
  return render(request, 'pack1/upload.html', {'form': form})

def delete_pack1(request, slug):
  if request.method == 'POST':
    video = Pack1.objects.get(slug=slug)
    poster = Pack1.objects.get(slug=slug)
    cloudinary.uploader.destroy(video.video.public_id, resource_type='video')
    cloudinary.uploader.destroy(poster.poster.public_id, resource_type='image')
    instance = Pack1.objects.get(slug=slug)
    instance.delete()
  return redirect('pack1')