from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from announcement.models import Announcement, Category, Images, Comment
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.get(pk=2)
    sliderdata = Announcement.objects.all()[:15]
    category = Category.objects.all()
    homepageAnnouncement = Announcement.objects.all().order_by('?')[:6]

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'homepageAnnouncement': homepageAnnouncement}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=2)
    from unicodedata import category
    context = {'setting': setting, 'category': category}
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
    from unicodedata import category
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)

    # def show_category(request):
    # return render(request, "header.html", {'category': Category.objects.all()})


def sponsor(request):
    setting = Setting.objects.get(pk=2)
    from unicodedata import category
    context = {'setting': setting, 'category': category}
    return render(request, 'sponsor.html', context)


def category_announcements(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    announcements = Announcement.objects.filter(category_id=id)
    context = {'announcements': announcements,
               'category': category,
               'categorydata': categorydata}
    return render(request, 'announcements.html', context)


def announcement_detail(request, id, slug):
    setting = Setting.objects.get(pk=2)
    category = Category.objects.all()
    announcements = Announcement.objects.get(pk=id)
    images = Images.objects.filter(announcement_id=id)
    comments = Comment.objects.filter(announcement_id=id, status='True')
    context = {'setting ': setting,
               'announcements': announcements,
               'category': category,
               'images': images,
               'comments': comments}
    return render(request, 'announcement_detail.html', context)


def announcement_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            announcements = Announcement.objects.filter(title_icontains=query)
            context = {'announcements': announcements,
                       'category': category}
            return render(request, 'announcement_search.html', context)

    return HttpResponseRedirect('/')

