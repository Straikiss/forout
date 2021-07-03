from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pack1, name='pack1'),
    path('uploadpack1/', views.upload_pack1, name='upload_pack1'),
    path('<slug>', views.video_pack1, name='video_pack1'),
    path('delete/<slug>', views.delete_pack1, name='delete_pack1'),
]