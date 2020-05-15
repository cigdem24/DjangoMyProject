from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from announcement.models import CommentForm, Comment, Announcement, Category, Images, ImagesForm
from menu.models import Menu
from home.models import UserProfile, Setting


def index(request):
    return HttpResponse("Announcement Page")


@login_required(login_url='/login')
def addcomment(request, id):
    current_user_profil = UserProfile.objects.get(user_id=request.user.id)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.userprofil = current_user_profil
            data.announcement_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarılı bir şekilde gönderilmiştir")
            return HttpResponseRedirect(url)

    messages.warning(request, "Yorumunuz kaydedilmedi. Lütfen Kontrol Ediniz")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def gallery(request, id):
    images = Images.objects.filter(announcement_id=id)
    form = ImagesForm()
    context = {
        'images': images,
        'id': id,
        'form': form,
    }

    return render(request, 'gallery.html', context)


@login_required(login_url='/login')
def galleryadd(request, id):
    if request.method == 'POST':  # form post edildiyse
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            data = Images()
            data.title = form.cleaned_data['title']
            data.image = form.cleaned_data['image']
            data.announcement_id = id
            data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
def gallerydelete(request, id):
    Images.objects.get(pk=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
