from django.db import models
from django.contrib.auth.models import User


class Blogtopic(models.Model):
    blogtext = models.CharField(max_length=200)
    blogdate_added = models.DateTimeField(auto_now_add=True)
    # blogowner=models.ForeignKey(User, on_delete=models.CASCADE)
    blogtopicimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        return self.blogtext


class Blogentry(models.Model):
    blogtopic = models.ForeignKey(Blogtopic, on_delete=models.CASCADE)
    blogentryowner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogentryowner')
    blogtitle = models.CharField(max_length=150)
    blogtext = models.TextField()
    blogdate_added = models.DateTimeField(auto_now_add=True)
    bloglike = models.ManyToManyField(User, blank=True)
    blogentryimage = models.ImageField(upload_to='images', default='images/defaultimage.png', blank=True, null=True)

    def __str__(self):
        # возвращает строковое представление модели
        if len(self.blogtext) > 50:
            return self.blogtext[:50] + '...'
        else:
            return self.blogtext


class Blogcomment(models.Model):
    blogpost = models.ForeignKey(Blogentry, on_delete=models.CASCADE, related_name='blogcomments')
    blogname = models.ForeignKey(User, on_delete=models.CASCADE)
    blogbody = models.TextField()
    blogcreated = models.DateTimeField(auto_now_add=True)
    blogupdated = models.DateTimeField(auto_now=True)
    blogactive = models.BooleanField(default=True)
