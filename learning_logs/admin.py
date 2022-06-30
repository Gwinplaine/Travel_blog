from django.contrib import admin

from learning_logs.models import Topic, Entry, Comment, Resttype

# регистрация Topic в админке
admin.site.register(Topic)
admin.site.register(Resttype)


# указание колонок для Entry в админке
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'date_added')


# указание колонок, фильтра и полей поиска для Comment в админке
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'updated', 'body', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')


# регистрация Comment и Entry в админке
admin.site.register(Comment, CommentAdmin)
admin.site.register(Entry, EntryAdmin)
