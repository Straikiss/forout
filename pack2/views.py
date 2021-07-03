from django.shortcuts import render, redirect
from .models import Pack2
from .import forms
import cloudinary.uploader
import cloudinary


def index_pack2(request):
  video = Pack2.objects.count()
  videos = Pack2.objects.all()
  return render(request, 'pack2/videos.html', {'videos': videos, 'video': video})

def video_pack2(request, slug):
  video = Pack2.objects.get(slug=slug)
  videos = Pack2.objects.all()
  return render(request, 'pack2/video.html', {'videos': videos, 'video': video})

def upload_pack2(request):
  if request.method == 'POST':
    form = forms.CreatePack2(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
  else:
    form = forms.CreatePack2()
  return render(request, 'pack2/upload.html', {'form': form})

def delete_pack2(request, slug):
  if request.method == 'POST':
    video = Pack2.objects.get(slug=slug)
    poster = Pack2.objects.get(slug=slug)
    cloudinary.uploader.destroy(video.video.public_id, resource_type='video')
    cloudinary.uploader.destroy(poster.poster.public_id, resource_type='image')
    instance = Pack2.objects.get(slug=slug)
    instance.delete()
  return redirect('pack2')