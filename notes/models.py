from django.db import models
from django.contrib.auth.models import User


class Notesentry(models.Model):
    '''информация, изученная по теме'''
    notestitle = models.CharField(max_length=50)
    notestext = models.TextField()
    notesdate_added = models.DateTimeField(auto_now_add=True)
    notesowner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''возвращает строковое представление модели'''
        if len(self.notestext) > 50:
            return self.notestext[:50] + '...'
        else:
            return self.notestext
