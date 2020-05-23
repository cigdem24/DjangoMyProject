from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from menu.models import Menu

# Create your views here.


from announcement.models import Category, Comment, AnnouncementForm, Announcement
from home.models import UserProfile, Setting
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    setting = Setting.objects.get(pk=2)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    menu = Menu.objects.all()
    context = {'category': category,
               'profile': profile,
               'menu': menu,
               'setting': setting
               }
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Account has been updated!')
            return redirect('/user')

    else:
        setting = Setting.objects.get(pk=2)
        category = Category.objects.all()
        menu = Menu.objects.all()
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form,
                   'menu': menu,
                   'setting': setting
                   }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        setting = Setting.objects.get(pk=2)
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        menu = Menu.objects.all()
        return render(request, 'change_password.html', {'form': form, 'category': category, 'menu': menu,'setting': setting})


@login_required(login_url='/login')
def comments(request):
    setting = Setting.objects.get(pk=2)
    menu = Menu.objects.all()
    category = Category.objects.all()
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comment': comment,
               'menu': menu,
               'setting': setting}
    return render(request, 'user_comments.html', context)


login_required(login_url='/login')


def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Announcement()
            data.user_id = current_user.id
            data.announcements_id = id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.category = form.cleaned_data['category']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'Your Content Recorded Successfully ')
            return HttpResponseRedirect('/user/announcements')
        else:
            messages.error(request, 'Announcement Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addannouncement')
    else:
        setting = Setting.objects.get(pk=2)
        category = Category.objects.all()
        form = AnnouncementForm()
        menu = Menu.objects.all()
        context = {
            'category': category,
            'form': form,
            'menu': menu,
            'setting': setting
        }
        return render(request, 'user_addannouncement.html', context)


@login_required(login_url='/login')
def announcementedit(request, id):
    announcement = Announcement.objects.get(id=id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Announcement Updated Successfully ')
            return HttpResponseRedirect('/user/announcements')
        else:
            messages.error(request, 'Announcement Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/announcementedit' + str(id))
    else:
        setting = Setting.objects.get(pk=2)
        category = Category.objects.all()
        menu = Menu.objects.all()
        form = AnnouncementForm(instance=announcement)
        context = {
            'category': category,
            'form': form,
            'menu': menu,
            'setting': setting
        }
        return render(request, 'user_addannouncement.html', context)


@login_required(login_url='/login')
def announcement_show(request):
    setting = Setting.objects.get(pk=2)
    category = Category.objects.all()
    menu = Menu.objects.all()
    current_user = request.user
    announcement = Announcement.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'menu': menu,
        'announcement': announcement,
        'setting': setting
    }
    return render(request, 'user_announcements.html', context)


@login_required(login_url='/login')
def announcementdelete(request, id):
    current_user = request.user
    Announcement.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Content deleted..')
    return HttpResponseRedirect('/user/announcements')
