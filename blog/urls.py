from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('', views.default, name='default'),
    path('videos/', include('videos.urls')),
    path('pack1/', include('pack1.urls')),
    path('pack2/', include('pack2.urls')),
    path('pack3/', include('pack3.urls')),
    path('premium/', include('premium.urls')),
    path('contacts/', views.contacts, name="contacts"),
    path('login/', views._login, name='login'),
    path('logout/', views._logout, name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL)