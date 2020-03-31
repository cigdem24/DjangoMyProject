from django.contrib import admin

# Register your models here.
from announcement.models import Category, Announcement, Images

class AnnouncementImageInline(admin.TabularInline):
    model = Images
    extra = 3
    #galeri kas resimden olussun

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    inlines = [AnnouncementImageInline]
    #image tablosunda 5 tane resim eklenecek alan olustur.

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['image']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Images,ImagesAdmin)
