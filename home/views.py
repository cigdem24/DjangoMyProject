from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from announcement.models import Announcement, Category
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.get(pk=2)
    sliderdata = Announcement.objects.all()[:15]
    category = Category.objects.all()

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız gönderilmiştir.Teşekkür ederiz")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=2)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


#def show_category(request):
    #return render(request, "header.html", {'category': Category.objects.all()})
