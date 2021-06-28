from django import forms
from .models import Blogtopic, Blogentry, Blogcomment

class BlogtopicForm(forms.ModelForm):
    class Meta:
        model = Blogtopic
        fields = ['blogtext']
        labels = {'blogtext': ''}

class BlogentryForm(forms.ModelForm):
    class Meta:
        model = Blogentry
        fields = ['blogtitle', 'blogtext']
        labels = {'blogtitle':'Название статьи','blogtext': 'Текст статьи'}
        widgets = {'blogtext': forms.Textarea(attrs={'cols': 80})}

class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = Blogcomment
        fields = ['blogbody']
        labels = {'blogbody': ''}