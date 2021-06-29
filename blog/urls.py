from . import views
from django.urls import path
from django.conf.urls import url
app_name = "blog"

urlpatterns = [
       url(r'^blogtopics/$', views.blogtopics, name='blogtopics'),
       url(r'^blogtopics/(?P<blogtopic_id>\d+)/$', views.blogtopic, name='blogtopic'),
       url(r'^new_blogentry/(?P<blogtopic_id>\d+)/$', views.new_blogentry, name='new_blogentry'),
       url(r'^edit_blogentry/(?P<blogentry_id>\d+)/$', views.edit_blogentry, name='edit_blogentry'),
       url(r'^blogentry/(?P<blogentry_id>\d+)/$', views.blogentry, name='blogentry'),
       url(r'^blogentry/(?P<blogentry_id>\d+)/add_to_fav/$', views.add_to_fav, name='add_to_fav'),
       url(r'^blogentry/(?P<blogentry_id>\d+)/remove_from_fav/$', views.remove_from_fav, name='remove_from_fav'),
       url(r'edit_blogcomment/(?P<blogentry_id>\d+)/(?P<blogcomment_id>\d+)/$', views.edit_blogcomment, name='edit_blogcomment'),
       url(r'^blogfavourites/$', views.blogfavourites, name='blogfavourites'),
       url(r'^delete_blogentry/(?P<blogtopic_id>\d+)/(?P<blogentry_id>\d+)/$', views.delete_blogentry, name='delete_blogentry'),
]