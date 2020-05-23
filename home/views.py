from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from django.contrib.auth import logout, login, authenticate
from announcement.models import Announcement, Category, Images, Comment
from home.models import *
from menu.models import Content, Menu
from .forms import SearchForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    setting = Setting.objects.get(pk=2)
    menu = Menu.objects.all()
    user = User.objects.all()
    userprofil = UserProfile.objects.all()
    sliderdata = Announcement.objects.all()[:7]
    latestdata = Announcement.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    homepageAnnouncement = Announcement.objects.all().order_by('?')[:6]
    content = Content.objects.all()

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'latestdata': latestdata,
               'category': category,
               'homepageAnnouncement': homepageAnnouncement,
               'menu': menu,
               'userprofil': userprofil,
               'content': content,

               }
    return render(request, 'index.html', context)


def about(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=2)

    context = {'setting': setting, 'category': category, 'menu': menu}
    return render(request, 'about.html', context)


def contact(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
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
    context = {'setting': setting, 'form': form, 'category': category, 'menu': menu}
    return render(request, 'contact.html', context)


def sponsor(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=2)
    context = {'setting': setting, 'category': category, 'menu': menu}
    return render(request, 'sponsor.html', context)


def category_announcements(request, id, slug):
    setting = Setting.objects.get(pk=2)
    menu = Menu.objects.all()
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    announcements = Announcement.objects.filter(category_id=id)
    context = {
        'setting': setting,
        'announcements': announcements,
        'category': category,
        'categorydata': categorydata,
        'menu': menu}
    return render(request, 'announcements.html', context)


def announcement_detail(request, id, slug):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=2)
    category = Category.objects.all()
    announcements = Announcement.objects.get(pk=id)
    images = Images.objects.filter(announcement_id=id)
    comments = Comment.objects.filter(announcement_id=id, status='True')
    context = {
        'setting': setting,
        'announcements': announcements,
        'category': category,
        'default': images,
        'comments': comments,
        'menu': menu,
        'images': images,
    }
    return render(request, 'announcement_detail.html', context)



def announcement_search(request):
    if request.method == 'POST':  # post edilip edilmemesi
        form = SearchForm(request.POST)  # search formunu çağırıyor
        if form.is_valid():
            menu = Menu.objects.all()
            category = Category.objects.all()
            setting = Setting.objects.get(pk=2)
            query = form.cleaned_data['query']  # formdan gelen veriyi query nesnesine ekledi
            announcements = Announcement.objects.filter(title__icontains=query)
            context = {'announcements': announcements,
                       'setting': setting,
                       'query': query,
                       'category': category, 'menu': menu}
            return render(request, 'announcement_search.html', context)
    return HttpResponseRedirect('/')


def announcement_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        announcement = Announcement.objects.filter(title__icontains=q)
        results = []
        for rs in announcement:
            announcement_json = {}
            announcement_json = rs.title
            results.append(announcement_json)
        data = json.dumps(results)
        print("Girdi" + str(data))
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, "Giriş yapamadınız.Lütfen bilgilerinizi kontrol ediniz.")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=2)
    context = {'category': category, 'menu': menu,'setting': setting,}

    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.image = "default/account-512.png"
            user_profile.save()
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    menu = Menu.objects.all()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=2)
    context = {
        'category': category,
        'form': form,
        'menu': menu,
        'setting': setting,
    }

    return render(request, 'signup.html', context)


def menu(request, id):
    try:
        content = Content.objects.get(menu_id=id)
        link = '/menu' + "/" + str(content.id) + "/" + str(content.slug)
        return HttpResponseRedirect(link)

    except:
        messages.warning(request, "ERROR ! İlgili İçerik Bulunamadı")
        link = '/home'
        return HttpResponseRedirect(link)


def content_detail(request, id, slug):
    category = Category.objects.all()
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    setting = Setting.objects.get(pk=2)

    context = {
        'category': category,
        'content': content,
        'menu': menu,
        'setting': setting
    }
    return render(request, 'content_detail.html', context)


def faq(request):
    category = Category.objects.all()
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=2)
    faq = FAQ.objects.all().order_by()
    context = {
        'category': category,
        'faq': faq,
        'menu': menu,
        'setting': setting
    }
    return render(request, 'faq.html', context)