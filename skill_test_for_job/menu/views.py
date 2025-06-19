from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


def index(request, path_name = None):
    return render(request, "index.html")