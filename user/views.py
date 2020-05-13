from django.contrib.auth.decorators import login_required
from form import form
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from content.models import Content, Menu, ContentForm

# Create your views here.


from announcement.models import Category, Comment
from home.models import UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    menu = Menu.objects.all()
    context = {'category': category,
               'profile': profile,
               'menu': menu
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
        category = Category.objects.all()
        menu = Menu.objects.all()
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form,
                   'menu': menu
                   }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        user_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        menu = Menu.objects.all()
        return render(request, 'change_password.html', {'form': form, 'category': category, 'menu': menu})


@login_required(login_url='/login')
def comments(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comment': comment,
               'menu': menu}
    return render(request, 'user_comments.html', context)


login_required(login_url='/login')


def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def addcontent(request):
    content = Content.objects.all()
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.type = form.cleaned_data['type']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'True'
            data.save()
            messages.success(request, 'Your Content Recorded Successfully ')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        category = Category.objects.all()
        form = ContentForm()
        menu = Menu.objects.all()
        context = {

            'category': category,
            'form': form,
            'menu': menu,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')
def contentedit(request, id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Content Updated Successfully ')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/contentedit' + str(id))
    else:
        category = Category.objects.all()
        menu = Menu.objects.all()
        form = ContentForm(instance=content)
        context = {
            'category': category,
            'form': form,
            'menu': menu,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    menu = Menu.objects.all()
    current_user = request.user
    content = Content.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'menu': menu,
        'content': content,
    }
    return render(request, 'user_contents.html', context)


@login_required(login_url='/login')
def contentdelete(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Content deleted..')
    return HttpResponseRedirect('/user/contents')
