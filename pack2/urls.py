from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pack2, name='pack2'),
    path('uploadpack2/', views.upload_pack2, name='upload_pack2'),
    path('<slug>', views.video_pack2, name='video_pack2'),
    path('delete/<slug>', views.delete_pack2, name='delete_pack2'),
]