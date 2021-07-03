from django import forms
from .models import Topic, Entry, Comment


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'topicimage']
        labels = {'text': 'Название раздела', 'topicimage':'Загрузите изображение'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'entryimage']
        labels = {'title': 'Название статьи', 'text': 'Содержимое статьи', 'entryimage':'Загрузите изображение'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': ''}
