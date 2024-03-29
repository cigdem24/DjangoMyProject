from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.


from announcement.models import Category, Announcement, Images, Comment


class AnnouncementImageInline(admin.TabularInline):
    model = Images
    extra = 3
    # galeri kas resimden olussun


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    list_filter = ['status']
    inlines = [AnnouncementImageInline]
    # image tablosunda 5 tane resim eklenecek alan olustur.
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    list_filter = ['image']
    readonly_fields = ('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_announcements_count', 'related_announcements_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Announcement,
            'category',
            'announcements_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Announcement,
                                                'category',
                                                'announcements_count',
                                                cumulative=True)
        return qs

    def related_announcements_count(self, instance):
        return instance.announcements_count

    related_announcements_count.short_description = 'Related products (for this specific category)'

    def related_announcements_cumulative_count(self, instance):
        return instance.announcements_cumulative_count

    related_announcements_cumulative_count.short_description = 'Related products (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'announcement', 'user', 'status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)
