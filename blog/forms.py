from django import forms
from .models import Blogtopic, Blogentry, Blogcomment


# форма для модели Blogtopic с указанием полей и их обозначениями
class BlogtopicForm(forms.ModelForm):
    class Meta:
        model = Blogtopic
        fields = ['blogtext', 'blogtopicimage']
        labels = {'blogtext': 'Название раздела', 'blogtopicimage': 'Загрузите изображение'}


# форма для модели Blogentry с указанием полей и их обозначениями
class BlogentryForm(forms.ModelForm):
    class Meta:
        model = Blogentry
        fields = ['blogtitle', 'blogtext', 'blogentryimage']
        labels = {'blogtitle': 'Название статьи', 'blogtext': 'Текст статьи', 'blogentryimage': 'Загрузите изображение'}
        widgets = {'blogtext': forms.Textarea(attrs={'cols': 80})}


# форма для модели Blogcomment с указанием полей и их обозначениями
class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = Blogcomment
        fields = ['blogbody']
        labels = {'blogbody': ''}
