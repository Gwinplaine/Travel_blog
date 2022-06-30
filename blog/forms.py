from django import forms
from .models import Blogtopic, Blogentry, Blogcomment, Blogresttype


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
        fields = ['blogtitle', 'blogtext', 'blogentryimage', 'blogtopic', 'blogresttypes']
        labels = {'blogtitle': 'Название статьи', 'blogtext': 'Текст статьи', 'blogentryimage': 'Загрузите изображение', 'blogtopic':'Выберите континент', 'blogresttypes':'Тип отдыха'}
        widgets = {'blogtext': forms.Textarea(attrs={'cols': 80})}


# форма для модели Blogcomment с указанием полей и их обозначениями
class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = Blogcomment
        fields = ['blogbody']
        labels = {'blogbody': ''}
