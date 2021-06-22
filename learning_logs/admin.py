from django.contrib import admin

from learning_logs.models import Topic, Entry, Comment
admin.site.register(Topic)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'date_added')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'updated', 'body', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
admin.site.register(Comment, CommentAdmin)
admin.site.register(Entry, EntryAdmin)
