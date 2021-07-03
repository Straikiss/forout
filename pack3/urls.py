from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pack3, name='pack3'),
    path('uploadpack3/', views.upload_pack3, name='upload_pack3'),
    path('<slug>', views.video_pack3, name='video_pack3'),
    path('delete/<slug>', views.delete_pack3, name='delete_pack3'),
]