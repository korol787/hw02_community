from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
