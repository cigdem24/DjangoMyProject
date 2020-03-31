from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text="Merhaba Django"
    context= {'text': text}
    return render(request, 'index.html',context)