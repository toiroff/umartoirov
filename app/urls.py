from django.urls import path
from .views import index,blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',index,name="home"),
  path('blog/<slug:slug>/',blog,name="blog"),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)