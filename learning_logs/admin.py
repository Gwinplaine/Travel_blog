from django.contrib import admin

from learning_logs.models import Topic, Entry, Comment
admin.site.register(Topic)
admin.site.register(Entry)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'body', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
admin.site.register(Comment, CommentAdmin)

