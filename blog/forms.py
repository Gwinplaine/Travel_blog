from django import forms
from .models import Blogtopic, Blogentry, Blogcomment

class BlogtopicForm(forms.ModelForm):
    class Meta:
        model = Blogtopic
        fields = ['blogtext', 'blogtopicimage']
        labels = {'blogtext': 'Название раздела', 'blogtopicimage':'Загрузите изображение'}

class BlogentryForm(forms.ModelForm):
    class Meta:
        model = Blogentry
        fields = ['blogtitle', 'blogtext', 'blogentryimage']
        labels = {'blogtitle':'Название статьи','blogtext': 'Текст статьи', 'blogentryimage':'Загрузите изображение'}
        widgets = {'blogtext': forms.Textarea(attrs={'cols': 80})}

class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = Blogcomment
        fields = ['blogbody']
        labels = {'blogbody': ''}