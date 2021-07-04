from django.contrib import admin

from blog.models import Blogtopic, Blogentry, Blogcomment

# регистрация Blogtopic в админке
admin.site.register(Blogtopic)


# указание колонок для Blogentry в админке
class BlogentryAdmin(admin.ModelAdmin):
    list_display = ('blogtitle', 'blogtopic', 'blogdate_added')


# указание колонок, фильтра и полей поиска для Blogcomment в админке
class BlogcommentAdmin(admin.ModelAdmin):
    list_display = ('blogname', 'blogpost', 'blogcreated', 'blogupdated', 'blogbody', 'blogactive')
    list_filter = ('blogactive', 'blogcreated', 'blogupdated')
    search_fields = ('blogname', 'blogbody')


# регистрация Blogcomment и Blogentry в админке
admin.site.register(Blogcomment, BlogcommentAdmin)
admin.site.register(Blogentry, BlogentryAdmin)
