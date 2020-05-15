from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from menu.models import Menu, Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'create_at']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'status',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
