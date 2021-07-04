from django import forms
from .models import Notesentry


# форма для модели Notesentry с указанием полей и их обозначениями
class NotesentryForm(forms.ModelForm):
    class Meta:
        model = Notesentry
        fields = ['notestitle', 'notestext']
        labels = {'notestitle': 'Название', 'notestext': 'Заметка'}
        widgets = {'notestext': forms.Textarea(attrs={'cols': 80})}
