from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    '''Тема, которую изучает пользователь'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topicimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''информация, изученная по теме'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True)
    entryimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''возвращает строковое представление модели'''
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text


class Comment(models.Model):
    post = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # class Meta:
    #    ordering = ('created',)

    # def __str__(self):
    #    return 'Comment by {} on {}'.format(self.name, self.post)
