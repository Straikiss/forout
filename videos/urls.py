from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_videos, name='videos'),
    path('uploadvideos/', views.upload_videos, name='upload_videos'),
    path('<slug>', views.video_videos, name='video_videos'),
    path('delete/<slug>', views.delete_videos, name='delete_videos'),
]