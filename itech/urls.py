from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='itech'),
    path('daftar', views.daftar_view, name='daftar'),
    path('daftar/valorant', views.daftar_valorant_view, name='daftar-valorant'),
    path('daftar/shortmovie', views.daftar_short_movie_view,
         name='daftar-shortmovie'),
    path('daftar/valorant/sukses', views.daftarsuksesvalorant_view,
         name='daftar-sukses-valorant'),
    path('daftar/shortmovie/sukses', views.daftarsuksesshortmovie_view,
         name='daftar-sukses-shortmovie'),
    path('about', views.about_view, name='about-itech'),
    path('juknis', views.juknis_view, name='juknis'),
    path('agenda', views.agenda_view, name='agenda'),
    path('faq', views.faq_view, name='faq'),
    path('kontak', views.kontak_view, name='kontak'),
    path('timeline', views.timeline_view, name='timeline'),
]
