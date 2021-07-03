from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_premium, name='premium'),
    path('uploadpremium/', views.upload_premium, name='upload_premium'),
    path('<slug>', views.video_premium, name='video_premium'),
    path('delete/<slug>', views.delete_premium, name='delete_premium'),
]