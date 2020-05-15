from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>/', views.deletecomment, name='deletecomment'),
    path('announcements/', views.announcement_show, name='announcement_show'),
    path('addannouncement/', views.add_announcement, name='add_announcement'),
    path('announcementedit/<int:id>/', views.announcementedit, name='announcementedit'),
    path('announcementdelete/<int:id>/', views.announcementdelete, name='announcementdelete'),
]