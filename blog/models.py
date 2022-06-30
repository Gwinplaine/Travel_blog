from django.db import models
from django.contrib.auth.models import User


# создание модели раздела Blogtopic с указанием названия раздела, датой добавления и изображением раздела
class Blogtopic(models.Model):
    blogtext = models.CharField(max_length=200)
    blogdate_added = models.DateTimeField(auto_now_add=True)
    blogtopicimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        return self.blogtext

class Blogresttype(models.Model):
    blogtext = models.CharField(max_length=50)
    blogtopicimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        return self.blogtext
# создание модели статей Blogentry с указанием привязанного к статье раздела, автора статьи, названия статьи,
# текста статьи, даты добавления статьи, атрибута like (ответственного за добавление в избранное) и привязанного
# к статье изображения
class Blogentry(models.Model):
    blogtopic = models.ForeignKey(Blogtopic, on_delete=models.CASCADE)
    blogentryowner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogentryowner')
    blogresttypes = models.ForeignKey(Blogresttype, on_delete=models.CASCADE, blank=True, null=True)
    blogtitle = models.CharField(max_length=150)
    blogtext = models.TextField()
    blogdate_added = models.DateTimeField(auto_now_add=True)
    bloglike = models.ManyToManyField(User, blank=True)
    blogentryimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    # возвращает представление текста как 'текст'+'...', если длина статьи составляет более 50 знаков
    def __str__(self):
        # возвращает строковое представление модели
        if len(self.blogtext) > 50:
            return self.blogtext[:50] + '...'
        else:
            return self.blogtext


# создание модели комментариев Blogcomment с указанием привязанной к комментарию статьи, привязанного автора
# комментария, текста комментария, даты добавления комментария, даты обновления комментария, активного состояния комментария
class Blogcomment(models.Model):
    blogpost = models.ForeignKey(Blogentry, on_delete=models.CASCADE, related_name='blogcomments')
    blogname = models.ForeignKey(User, on_delete=models.CASCADE)
    blogbody = models.TextField()
    blogcreated = models.DateTimeField(auto_now_add=True)
    blogupdated = models.DateTimeField(auto_now=True)
    blogactive = models.BooleanField(default=True)
