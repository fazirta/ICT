from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models
from .forms import PendaftaranValorantForm
from .forms import PendaftaranShortMovieForm

# Create your views here.


def home_view(request):
    contexts = {}
    return render(request, 'itech/home.html', contexts)


def about_view(request):
    contexts = {}
    return render(request, 'itech/about.html', contexts)


def juknis_view(request):
    contexts = {}
    return render(request, 'itech/juknis.html', contexts)


def agenda_view(request):
    contexts = {}
    return render(request, 'itech/agenda.html', contexts)


def faq_view(request):
    contexts = {}
    return render(request, 'itech/faq.html', contexts)


def kontak_view(request):
    contexts = {}
    return render(request, 'itech/kontak.html', contexts)


def daftar_view(request):
    context = {
    }
    return render(request, 'itech/daftar.html', context)


def daftar_valorant_view(request):
    form = PendaftaranValorantForm()

    if request.method == 'POST':
        form = PendaftaranValorantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='daftar-sukses-valorant')

    context = {
        'form': form,
    }
    return render(request, 'itech/daftar-valorant.html', context)


def daftar_short_movie_view(request):
    form = PendaftaranShortMovieForm()

    if request.method == 'POST':
        form = PendaftaranShortMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='daftar-sukses-shortmovie')

    context = {
        'form': form,
    }
    return render(request, 'itech/daftar-shortmovie.html', context)


def daftarsuksesvalorant_view(request):
    context = {}
    return render(request, 'itech/daftar-sukses-valorant.html', context)


def daftarsuksesshortmovie_view(request):
    context = {}
    return render(request, 'itech/daftar-sukses-shortmovie.html', context)

def timeline_view(request):
    context = {}
    return render(request, 'itech/timeline.html', context)
