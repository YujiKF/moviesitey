from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)