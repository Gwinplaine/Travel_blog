from django.contrib import admin

from blog.models import Blogtopic, Blogentry, Blogcomment
admin.site.register(Blogtopic)


class BlogentryAdmin(admin.ModelAdmin):
    list_display = ('blogtitle', 'blogtopic', 'blogdate_added')

class BlogcommentAdmin(admin.ModelAdmin):
    list_display = ('blogname', 'blogpost', 'blogcreated', 'blogupdated', 'blogbody', 'blogactive')
    list_filter = ('blogactive', 'blogcreated', 'blogupdated')
    search_fields = ('blogname', 'blogbody')
admin.site.register(Blogcomment, BlogcommentAdmin)
admin.site.register(Blogentry, BlogentryAdmin)