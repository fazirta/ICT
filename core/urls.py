from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('fotografi', views.fotografi_view, name='fotografi'),
    path('videografi', views.videografi_view, name='videografi'),
    path('desaingrafis', views.desaingrafis_view, name='desaingrafis'),
    path('programming', views.programming_view, name='programming'),
    path('musicmaking', views.musicmaking_view, name='musicmaking'),
]
