"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', include('home.urls')),
    path('announcement/', include('announcement.urls')),
    path('home/', include('home.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_announcements, name='category_announcements'),
    path('announcement/<int:id>/<slug:slug>/', views.announcement_detail, name='announcement_detail'),
    path('search/', views.announcement_search, name='announcement_search'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
