from django import forms
from .models import Topic, Entry, Comment

# форма для модели Topic с указанием полей и их обозначениями
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'topicimage']
        labels = {'text': 'Название раздела', 'topicimage': 'Загрузите изображение'}

# форма для модели Entry с указанием полей и их обозначениями
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'entryimage','topic']
        labels = {'title': 'Название статьи', 'text': 'Содержимое статьи', 'entryimage': 'Загрузите изображение'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# форма для модели Comment с указанием полей и их обозначениями
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': ''}
