from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# создание модели раздела Topic с указанием названия раздела, создателя раздела, датой добавления и изображением раздела
class Topic(models.Model):
    text = models.CharField(max_length=50)
    
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topicimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        return self.text




# создание модели статей Entry с указанием привязанного к статье раздела, автора статьи, названия статьи,
# текста статьи, даты добавления статьи, атрибута like (ответственного за добавление в избранное) и привязанного
# к статье изображения
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True)
    entryimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)
        

    # указание множественного числа названия класса
    class Meta:
        verbose_name_plural = 'entries'

    # возвращает представление текста как 'текст'+'...', если длина статьи составляет более 50 знаков
    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text


# создание модели комментариев Comment с указанием привязанной к комментарию статьи, привязанного автора
# комментария, текста комментария, даты добавления комментария, даты обновления комментария, активного состояния
# комментария
class Comment(models.Model):
    post = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
