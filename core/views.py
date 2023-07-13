from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from . import models

def home_view(request):
    template = 'core/home.html'

    contexts = {
        'authenticated': request.user.is_authenticated
    }
    return render(request, template, contexts)

def about_view(request):
    template = 'core/about.html'

    contexts = {}
    return render(request, template, contexts)

def fotografi_view(request):
    template = 'core/divisi/fotografi.html'

    contexts = {}
    return render(request, template, contexts)

def videografi_view(request):
    template = 'core/divisi/videografi.html'

    contexts = {}
    return render(request, template, contexts)

def desaingrafis_view(request):
    template = 'core/divisi/desaingrafis.html'

    contexts = {}
    return render(request, template, contexts)

def programming_view(request):
    template = 'core/divisi/programming.html'

    contexts = {}
    return render(request, template, contexts)

def musicmaking_view(request):
    template = 'core/divisi/musicmaking.html'

    contexts = {}
    return render(request, template, contexts)

def handler404(request, *args, **argv):
    response = render(request, 'core/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'core/500.html')
    response.status_code = 500
    return response
