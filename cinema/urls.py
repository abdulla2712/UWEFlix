from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<movie_id>', views.movie, name='movie'),
    path('video',views.video,name='video')
]
