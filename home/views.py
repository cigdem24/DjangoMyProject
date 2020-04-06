from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting}
    return render(request, 'contact.html', context)