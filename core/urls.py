
from django.contrib import admin
from django.urls import path
from movie.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)