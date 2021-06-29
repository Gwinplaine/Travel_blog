from django import forms
from .models import Topic, Entry, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Название раздела'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'title':'Название статьи', 'text': 'Содержимое статьи'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': ''}